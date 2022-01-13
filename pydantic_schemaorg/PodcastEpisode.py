from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Episode import Episode


class PodcastEpisode(Episode):
    """A single episode of a podcast series.

    See: https://schema.org/PodcastEpisode
    Model depth: 4
    """

    type_: str = Field("PodcastEpisode", const=True, alias="@type")


if TYPE_CHECKING:

    PodcastEpisode.update_forward_refs()
