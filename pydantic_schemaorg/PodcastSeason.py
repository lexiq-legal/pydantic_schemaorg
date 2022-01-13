from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason


class PodcastSeason(CreativeWorkSeason):
    """A single season of a podcast. Many podcasts do not break down into separate seasons. In"
     "that case, PodcastSeries should be used.

    See: https://schema.org/PodcastSeason
    Model depth: 4
    """

    type_: str = Field("PodcastSeason", const=True, alias="@type")


if TYPE_CHECKING:

    PodcastSeason.update_forward_refs()
