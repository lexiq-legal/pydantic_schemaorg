from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post.

    See https://schema.org/BlogPosting.

    """
    type_: str = Field("BlogPosting", const=True, alias='@type')
    

BlogPosting.update_forward_refs()
