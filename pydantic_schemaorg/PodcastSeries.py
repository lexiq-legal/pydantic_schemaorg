from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class PodcastSeries(CreativeWorkSeries):
    """A podcast is an episodic series of digital audio or video files which a user can download"
     "and listen to.

    See: https://schema.org/PodcastSeries
    Model depth: 4
    """
    type_: str = Field("PodcastSeries", alias='@type')
    webFeed: Optional[Union[List[Union[AnyUrl, 'URL', 'DataFeed', str]], AnyUrl, 'URL', 'DataFeed', str]] = Field(
        None,
        description="The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped"
     "updates. This is usually RSS or Atom.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DataFeed import DataFeed
    from pydantic_schemaorg.Person import Person
