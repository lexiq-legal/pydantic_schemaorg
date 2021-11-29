from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class DiscussionForumPosting(SocialMediaPosting):
    """A posting to a discussion forum.

    See https://schema.org/DiscussionForumPosting.

    """

    locals().update({"@type": Field("DiscussionForumPosting", const=True)})


DiscussionForumPosting.update_forward_refs()
