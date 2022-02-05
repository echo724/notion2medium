from pydoc import describe
from cleo.commands.command import Command
from cleo.helpers import option

class PublishCommand(Command):
    name = "publish"
    description = "Publish a <c2>Notion</c2> page to publish to Medium."
    help = """You can publish a Notion page from Notion Database that will be published to Medium.
    """
    options = [
        option(
            "id",
            "i",
            "id of the Notion page object",
            flag = False,
        ),
        option(
            "url",
            "u",
            "url of the Notion page object",
            flag = False,
        ),
    ]

    def handle(self) -> int:
        id = self.option('id')
        self.line(f"Hello {id}")