from pydantic import Field
from pydantic_schemaorg.Episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series.

    See https://schema.org/PodcastEpisode.

    """

    locals().update({"@type": Field("PodcastEpisode", const=True)})


PodcastEpisode.update_forward_refs()
