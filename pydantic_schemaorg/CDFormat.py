from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CDFormat(MusicReleaseFormatType):
    """CDFormat.

    See https://schema.org/CDFormat.

    """
    type_: str = Field("CDFormat", const=True, alias='@type')
    

CDFormat.update_forward_refs()
