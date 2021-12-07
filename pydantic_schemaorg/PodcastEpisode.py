from pydantic import Field
from pydantic_schemaorg.Episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series.

    See https://schema.org/PodcastEpisode.

    """
    type_: str = Field("PodcastEpisode", const=True, alias='@type')
    

PodcastEpisode.update_forward_refs()
