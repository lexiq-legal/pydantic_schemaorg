from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class LaserDiscFormat(MusicReleaseFormatType):
    """LaserDiscFormat.

    See https://schema.org/LaserDiscFormat.

    """

    locals().update({"@type": Field("LaserDiscFormat", const=True)})


LaserDiscFormat.update_forward_refs()
