from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post.

    See https://schema.org/BlogPosting.

    """

    locals().update({"@type": Field("BlogPosting", const=True)})


BlogPosting.update_forward_refs()
