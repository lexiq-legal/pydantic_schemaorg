from pydantic import Field
from pydantic_schemaorg.VisualArtwork import VisualArtwork


class CoverArt(VisualArtwork):
    """The artwork on the outer surface of a CreativeWork.

    See https://schema.org/CoverArt.

    """

    locals().update({"@type": Field("CoverArt", const=True)})


CoverArt.update_forward_refs()
