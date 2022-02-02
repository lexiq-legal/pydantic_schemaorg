from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class AmpStory(CreativeWork):
    """A creative work with a visual storytelling format intended to be viewed online, particularly"
     "on mobile devices.

    See: https://schema.org/AmpStory
    Model depth: 3
    """
    type_: str = Field("AmpStory", alias='@type')
    

