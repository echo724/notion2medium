from cleo.helpers import option
from notion_client.helpers import get_id

from notion2medium.exceptions import ClientTokenException

from .command import CustomCommand


class SelectCommand(CustomCommand):
    name = "select"
    description = "Select a <bold>Notion</bold> page from a database to be published to Medium."
    help = """
Select a <highlight>Notion</highlight> page from <highlight>Notion Database</highlight>
    that will be published to <highlight>Medium</highlight>.

<b>[Prerequisite]</b>

 - Export <highlight>Notion</highlight> and <highlight>Medium</highlight> Token to your shell config

    ex) Add those codes to your <code>.zshrc</code> or <code>.bashrc</code>

    <code>export $NOTION_TOKEN='{{ YOUR_TOKEN }}'</code>
    <code>export $MEDIUM_TOKEN='{{ YOUR_TOKEN }}'</code>

 - Your <highlight>Notion Integration</highlight> should be shared with your <highlight>Notion Database</highlight>.

"""
    options = [
        option(
            "id",
            "i",
            "id of the Notion database object",
            flag=False,
        ),
        option(
            "url",
            "u",
            "url of the Notion database object",
            flag=False,
        ),
    ]

    def __init__(self):
        super().__init__()
        self.database = {}

    def retrieve_database_from(self, database_id):
        self.line("")
        with self.indicator(
            start_message=self.output_ongoing("RETRIEVING", "Notion Database"),
            end_message=self.output_success("RETRIEVED", "Notion Database"),
        ):
            try:
                self.database = self.notion_client.get_database(
                    database_id=database_id
                )
            except ClientTokenException as e:
                self.output_error(e)

    def get_page_title(self):
        return list(
            map(
                lambda X: list(
                    v for k, v in X["properties"].items() if "title" in v
                )[0]["title"][0]["plain_text"],
                self.database["results"],
            )
        )

    def find_page_id_from_answer_in_titles(self, answer, titles):
        return self.database["results"][titles.index(answer)]["id"]

    def handle(self) -> int:
        database_id = self.parse_id_from_args()
        self.retrieve_database_from(database_id)
        titles = self.get_page_title()
        answer = self.choice(
            question=self.output_success(
                "SELECT", "a Notion page to be published to Medium"
            ),
            choices=titles,
        )

        self.clear_after_call(len(titles) + 2)
        self.line(self.output_success("SELECTED", f"[{self.info(answer)}]"))

        page_id = self.find_page_id_from_answer_in_titles(answer, titles)

        self.call("publish", (page_id, ",", answer))
