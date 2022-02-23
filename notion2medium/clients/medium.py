import os

from typing import List

from medium_sdk_python.medium import Client


class MediumClient(object):
    def __init__(self):
        self._client = Client(access_token=os.environ.get("MEDIUM_TOKEN"))
        self._user = self._client.get_current_user()

    def create_post(
        self,
        title: str,
        content: str,
        tags: List[str] = None,
        canonical_url: str = None,
        publish_status: str = "draft",
        license: str = None,
    ):
        self._client.create_post(
            user_id=self._user["id"],
            title=title,
            content=content,
            content_format="markdown",
            tags=tags,
            canonical_url=canonical_url,
            publish_status=publish_status,
            license=license,
        )
