from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Episode import Episode


class RadioEpisode(Episode):
    """A radio episode which can be part of a series or season.

    See: https://schema.org/RadioEpisode
    Model depth: 4
    """
    type_: str = Field("RadioEpisode", alias='@type')
    

