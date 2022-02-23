import sys

from cleo.commands.command import Command
from cleo.cursor import Cursor
from notion_client.helpers import get_id

from notion2medium.clients.medium import MediumClient
from notion2medium.clients.notion_client import NotionClient


class CustomCommand(Command):
    def __init__(self):
        super().__init__()
        self._cursor = None
        self._notion_client = None
        self._medium_client = None

    @property
    def medium_client(self):
        if not self._medium_client:
            self._medium_client = MediumClient()
        return self._medium_client

    @property
    def notion_client(self):
        if not self._notion_client:
            self._notion_client = NotionClient()
        return self._notion_client

    @property
    def cursor(self):
        if not self._cursor:
            self._cursor = Cursor(self.io._output)
        return self._cursor

    def parse_id_from_args(self):
        if self.option("id"):
            id_ = self.option("id")
        elif self.option("url"):
            id_ = get_id(self.option("url"))
        else:
            self.output_error("Notion2Medium requires either id or url.")
        return id_

    def reset_output(self):
        self.cursor.clear_screen()
        self.cursor.move_to_position(1, 1)

    def clear_after_call(self, lines: int = 0):
        self.cursor.move_up(lines)
        self.cursor.clear_output()

    def indicator(self, start_message, end_message):
        return self.progress_indicator(
            fmt="{message}{indicator}", values=["", "∙", "∙∙", "∙∙∙", "∙∙∙∙"]
        ).auto(start_message=start_message, end_message=end_message)

    def output_error(self, message):
        self.line("")
        self.line(f"{'[<success>ERROR</success>]':<32} {message}")
        self.line("")
        sys.exit(1)

    def output_success(self, status, message=None):
        return f" {f'[<success>{status}</success>]':<32} {message}"

    def output_ongoing(self, status, message=None):
        return f" {f'[<ongoing>{status}</ongoing>]':<32} {message}"

    def info(self, message):
        return f"<info>{message}</info>"
