from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Article import Article


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    See https://schema.org/SocialMediaPosting.

    """
    type_: str = Field("SocialMediaPosting", const=True, alias='@type')
    sharedContent: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )
    

SocialMediaPosting.update_forward_refs()
