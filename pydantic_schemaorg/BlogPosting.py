from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SocialMediaPosting import SocialMediaPosting


class BlogPosting(SocialMediaPosting):
    """A blog post.

    See: https://schema.org/BlogPosting
    Model depth: 5
    """

    type_: str = Field("BlogPosting", const=True, alias="@type")


if TYPE_CHECKING:

    BlogPosting.update_forward_refs()
