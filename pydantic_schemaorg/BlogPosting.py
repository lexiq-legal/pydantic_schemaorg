from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post.

    See: https://schema.org/BlogPosting
    Model depth: 5
    """
    type_: str = Field("BlogPosting", alias='@type')
    

