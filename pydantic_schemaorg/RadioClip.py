from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program.

    See: https://schema.org/RadioClip
    Model depth: 4
    """
    type_: str = Field("RadioClip", alias='@type')
    

