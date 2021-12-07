from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See https://schema.org/CassetteFormat.

    """
    type_: str = Field("CassetteFormat", const=True, alias='@type')
    

CassetteFormat.update_forward_refs()
