from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class MusicVideoObject(MediaObject):
    """A music video file.

    See: https://schema.org/MusicVideoObject
    Model depth: 4
    """
    type_: str = Field("MusicVideoObject", alias='@type')
    

