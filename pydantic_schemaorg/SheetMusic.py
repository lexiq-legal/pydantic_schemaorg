from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music.

    See: https://schema.org/SheetMusic
    Model depth: 3
    """
    type_: str = Field("SheetMusic", alias='@type')
    

