from pydantic import AnyUrl, Field
from pydantic_schemaorg.DataFeed import DataFeed
from typing import List, Optional, Union
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class PodcastSeries(CreativeWorkSeries):
    """A podcast is an episodic series of digital audio or video files which a user can download"
     "and listen to.

    See https://schema.org/PodcastSeries.

    """
    type_: str = Field("PodcastSeries", const=True, alias='@type')
    webFeed: Optional[Union[List[Union[AnyUrl, DataFeed, str]], Union[AnyUrl, DataFeed, str]]] = Field(
        None,
        description="The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped"
     "updates. This is usually RSS or Atom.",
    )
    actor: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    

PodcastSeries.update_forward_refs()
