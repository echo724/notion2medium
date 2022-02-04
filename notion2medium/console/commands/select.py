from pydoc import describe
from cleo.commands.command import Command

class SelectCommand(Command):
    name = "select"
    description = "Select a Notion page to publish to Medium."

    def handle(self) -> int:
        print("hello world")