import os

from notion_client import Client

from notion2medium.exceptions import ClientTokenException


class NotionClient(object):
    def __init__(self):
        try:
            self._client = Client(auth=os.environ.get("NOTION_TOKEN"))
        except Exception:
            raise ClientTokenException("Notion Client")

    def get_page(self, page_id):
        return self._client.pages.retrieve(page_id=page_id)

    def get_database(self, database_id, **query):
        return self._client.databases.query(database_id=database_id, **query)
