from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    See: https://schema.org/DiscussionForumPosting
    Model depth: 5
    """

    type_: str = Field("DiscussionForumPosting", const=True, alias="@type")


if TYPE_CHECKING:

    DiscussionForumPosting.update_forward_refs()
