from pydantic import Field
from pydantic_schema_org.MusicReleaseFormatType import MusicReleaseFormatType


class CDFormat(MusicReleaseFormatType):
    """CDFormat.

    See https://schema.org/CDFormat.

    """

    locals().update({"@type": Field("CDFormat", const=True)})


CDFormat.update_forward_refs()
