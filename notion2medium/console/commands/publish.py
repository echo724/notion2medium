from typing import List

from cleo.helpers import option
from medium_sdk_python.medium import MediumError
from notion2md.exporter.block import StringExporter

from notion2medium.exceptions import ClientTokenException

from .command import CustomCommand


class PublishCommand(CustomCommand):
    name = "publish"
    description = "Publish a Notion page to Medium."

    help = """
Publish a <highlight>Notion</highlight> page to <highlight>Medium</highlight>.

<b>[Prerequisite]</b>

 - Export <highlight>Notion</highlight> and <highlight>Medium</highlight> Token to your shell config

    ex) Add those codes to your <code>.zshrc</code> or <code>.bashrc</code>

    <code>export $NOTION_TOKEN='{{YOUR_TOKEN}}'</code>
    <code>export $MEDIUM_TOKEN='{{YOUR_TOKEN}}'</code>

 - Your <highlight>Notion Integration</highlight> should be shared with your <highlight>Notion Page</highlight>.
"""
    options = [
        option(
            "id",
            "i",
            "id of the Notion page object",
            flag=False,
        ),
        option(
            "url",
            "u",
            "url of the Notion page object",
            flag=False,
        ),
        option("tags"),
    ]

    def get_page_title_from(self, page: dict):
        return [
            value
            for key, value in page["properties"].items()
            if "title" in value
        ][0]["title"][0]["plain_text"]

    def get_page_id_title_from_args(self):
        command_arg: str = self.argument("command")
        if command_arg != "publish":
            page_id, page_title = command_arg.split(",")
        else:
            page_id = self.parse_id_from_args()
            page_title = "Notion Page"
        return page_id, page_title

    def get_tags_from(self, page: dict) -> List[str]:
        return list(
            map(
                lambda values: values["name"],
                page["properties"]["Tags"]["multi_select"],
            )
        )

    def inject_title_to_content(self, page_title, content):
        header = "".join(["# ", page_title, "\n\n"])
        content = "".join([header, content])
        return content

    def handle(self) -> int:
        self.line("")
        # Case1: id from select command
        page_id, page_title = self.get_page_id_title_from_args()

        # Common Case:
        # - get page object from notion_client
        try:
            with self.indicator(
                start_message=self.output_ongoing(
                    "RETRIEVING", f"{self.info(page_title)}'s properties"
                ),
                end_message=self.output_success(
                    "RETRIEVED", f"{self.info(page_title)}'s properties"
                ),
            ):
                page = self.notion_client.get_page(page_id)
        except ClientTokenException as e:
            self.output_error(e)
        if page_title == "Notion Page":
            page_title = self.get_page_title_from(page)
        # - parse tags
        page_tags = self.get_tags_from(page)
        # - call notion2md to get block object
        with self.indicator(
            start_message=self.output_ongoing(
                "RETRIEVING", f"{self.info(page_title)}'s content"
            ),
            end_message=self.output_success(
                "RETRIEVED", f"{self.info(page_title)}'s content"
            ),
        ):
            content = StringExporter(block_id=page_id, unzipped=True).export()
        # - inject title header to content
        content = self.inject_title_to_content(page_title, content)

        try:
            with self.indicator(
                start_message=self.output_ongoing(
                    "PUBLISHING", f"{self.info(page_title)} to Medium"
                ),
                end_message=self.output_success(
                    "PUBLISHED",
                    f"Successfully published {self.info(page_title)}",
                ),
            ):
                # - call medium to publish a post from params
                self.medium_client.create_post(
                    title=page_title,
                    content=content,
                    tags=page_tags,
                )
        except (ClientTokenException, MediumError) as e:
            self.output_error(e)
        self.line("")
