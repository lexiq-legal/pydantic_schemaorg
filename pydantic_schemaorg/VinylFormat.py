from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class VinylFormat(MusicReleaseFormatType):
    """VinylFormat.

    See https://schema.org/VinylFormat.

    """

    locals().update({"@type": Field("VinylFormat", const=True)})


VinylFormat.update_forward_refs()
