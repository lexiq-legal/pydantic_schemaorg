from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """An art gallery.

    See: https://schema.org/ArtGallery
    Model depth: 5
    """
    type_: str = Field("ArtGallery", alias='@type')
    

