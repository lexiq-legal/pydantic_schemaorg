from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose.

    See: https://schema.org/ShortStory
    Model depth: 3
    """
    type_: str = Field("ShortStory", alias='@type')
    

