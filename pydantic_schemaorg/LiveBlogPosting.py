from pydantic import Field
from datetime import datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.BlogPosting import BlogPosting


class LiveBlogPosting(BlogPosting):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage"
     "of an ongoing event through continuous updates.

    See https://schema.org/LiveBlogPosting.

    """

    coverageEndTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The time when the live blog will stop covering the Event. Note that coverage may continue"
     "after the Event concludes.",
    )
    liveBlogUpdate: Optional[Union[List[BlogPosting], BlogPosting]] = Field(
        None,
        description="An update to the LiveBlog.",
    )
    coverageStartTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The time when the live blog will begin covering the Event. Note that coverage may begin"
     "before the Event's start time. The LiveBlogPosting may also be created before coverage"
     "begins.",
    )
    locals().update({"@type": Field("LiveBlogPosting", const=True)})


LiveBlogPosting.update_forward_refs()
