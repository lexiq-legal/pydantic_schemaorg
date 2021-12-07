from pydantic import Field
from pydantic_schemaorg.VisualArtwork import VisualArtwork


class CoverArt(VisualArtwork):
    """The artwork on the outer surface of a CreativeWork.

    See https://schema.org/CoverArt.

    """
    type_: str = Field("CoverArt", const=True, alias='@type')
    

CoverArt.update_forward_refs()
