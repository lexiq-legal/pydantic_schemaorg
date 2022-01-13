from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Article import Article


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    See: https://schema.org/SocialMediaPosting
    Model depth: 4
    """

    type_: str = Field("SocialMediaPosting", const=True, alias="@type")
    sharedContent: "Optional[Union[List[Union[CreativeWork, str]], Union[CreativeWork, str]]]" = Field(
        None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.CreativeWork import CreativeWork

    SocialMediaPosting.update_forward_refs()
