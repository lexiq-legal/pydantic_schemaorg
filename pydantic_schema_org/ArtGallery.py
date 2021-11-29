from pydantic import Field
from pydantic_schema_org.EntertainmentBusiness import EntertainmentBusiness


class ArtGallery(EntertainmentBusiness):
    """An art gallery.

    See https://schema.org/ArtGallery.

    """

    locals().update({"@type": Field("ArtGallery", const=True)})


ArtGallery.update_forward_refs()
