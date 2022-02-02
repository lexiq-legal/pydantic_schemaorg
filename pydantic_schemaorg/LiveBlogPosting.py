from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.BlogPosting import BlogPosting


class LiveBlogPosting(BlogPosting):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage"
     "of an ongoing event through continuous updates.

    See: https://schema.org/LiveBlogPosting
    Model depth: 6
    """
    type_: str = Field("LiveBlogPosting", alias='@type')
    coverageEndTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The time when the live blog will stop covering the Event. Note that coverage may continue"
     "after the Event concludes.",
    )
    liveBlogUpdate: Optional[Union[List[Union['BlogPosting', str]], 'BlogPosting', str]] = Field(
        None,
        description="An update to the LiveBlog.",
    )
    coverageStartTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The time when the live blog will begin covering the Event. Note that coverage may begin"
     "before the Event's start time. The LiveBlogPosting may also be created before coverage"
     "begins.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.BlogPosting import BlogPosting
