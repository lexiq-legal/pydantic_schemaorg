from pydantic import Field
from pydantic_schema_org.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See https://schema.org/CassetteFormat.

    """

    locals().update({"@type": Field("CassetteFormat", const=True)})


CassetteFormat.update_forward_refs()
