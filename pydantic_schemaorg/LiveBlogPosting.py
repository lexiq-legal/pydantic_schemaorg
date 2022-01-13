from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.BlogPosting import BlogPosting


class LiveBlogPosting(BlogPosting):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage"
     "of an ongoing event through continuous updates.

    See: https://schema.org/LiveBlogPosting
    Model depth: 6
    """

    type_: str = Field("LiveBlogPosting", const=True, alias="@type")
    coverageEndTime: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="The time when the live blog will stop covering the Event. Note that coverage may continue"
        "after the Event concludes.",
    )
    liveBlogUpdate: "Optional[Union[List[Union[BlogPosting, str]], Union[BlogPosting, str]]]" = Field(
        None,
        description="An update to the LiveBlog.",
    )
    coverageStartTime: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="The time when the live blog will begin covering the Event. Note that coverage may begin"
        "before the Event's start time. The LiveBlogPosting may also be created before coverage"
        "begins.",
    )


if TYPE_CHECKING:

    from datetime import datetime

    from pydantic_schemaorg.BlogPosting import BlogPosting

    LiveBlogPosting.update_forward_refs()
