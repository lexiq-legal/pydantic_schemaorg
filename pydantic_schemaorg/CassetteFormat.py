from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See https://schema.org/CassetteFormat.

    """

    locals().update({"@type": Field("CassetteFormat", const=True)})


CassetteFormat.update_forward_refs()
