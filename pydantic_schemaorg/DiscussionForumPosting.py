from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    See: https://schema.org/DiscussionForumPosting
    Model depth: 5
    """
    type_: str = Field("DiscussionForumPosting", alias='@type')
    

