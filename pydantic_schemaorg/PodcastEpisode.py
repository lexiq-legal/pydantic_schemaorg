from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series.

    See: https://schema.org/PodcastEpisode
    Model depth: 4
    """
    type_: str = Field("PodcastEpisode", alias='@type')
    

