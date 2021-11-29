from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Article import Article


class SocialMediaPosting(Article):
    """A post to a social media platform, including blog posts, tweets, Facebook posts, etc.

    See https://schema.org/SocialMediaPosting.

    """

    sharedContent: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )
    locals().update({"@type": Field("SocialMediaPosting", const=True)})


SocialMediaPosting.update_forward_refs()
