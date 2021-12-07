from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    See https://schema.org/DiscussionForumPosting.

    """
    type_: str = Field("DiscussionForumPosting", const=True, alias='@type')
    

DiscussionForumPosting.update_forward_refs()
