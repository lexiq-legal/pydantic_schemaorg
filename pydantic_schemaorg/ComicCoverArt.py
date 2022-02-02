from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CoverArt import CoverArt
from pydantic_schemaorg.ComicStory import ComicStory


class ComicCoverArt(CoverArt, ComicStory):
    """The artwork on the cover of a comic.

    See: https://schema.org/ComicCoverArt
    Model depth: 4
    """
    type_: str = Field("ComicCoverArt", alias='@type')
    

