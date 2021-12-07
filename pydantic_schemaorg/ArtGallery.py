from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """An art gallery.

    See https://schema.org/ArtGallery.

    """
    type_: str = Field("ArtGallery", const=True, alias='@type')
    

ArtGallery.update_forward_refs()
