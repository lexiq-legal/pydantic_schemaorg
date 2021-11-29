from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """A single season of a podcast. Many podcasts do not break down into separate seasons. In"
     "that case, PodcastSeries should be used.

    See https://schema.org/PodcastSeason.

    """

    locals().update({"@type": Field("PodcastSeason", const=True)})


PodcastSeason.update_forward_refs()
