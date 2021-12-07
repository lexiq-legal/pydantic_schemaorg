from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class LaserDiscFormat(MusicReleaseFormatType):
    """LaserDiscFormat.

    See https://schema.org/LaserDiscFormat.

    """
    type_: str = Field("LaserDiscFormat", const=True, alias='@type')
    

LaserDiscFormat.update_forward_refs()
