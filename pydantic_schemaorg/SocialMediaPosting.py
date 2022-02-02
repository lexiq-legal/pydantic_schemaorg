from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Article import Article


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    See: https://schema.org/SocialMediaPosting
    Model depth: 4
    """
    type_: str = Field("SocialMediaPosting", alias='@type')
    sharedContent: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
