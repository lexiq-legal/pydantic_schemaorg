from pydantic import Field
from pydantic_schema_org.MusicReleaseFormatType import MusicReleaseFormatType


class DVDFormat(MusicReleaseFormatType):
    """DVDFormat.

    See https://schema.org/DVDFormat.

    """

    locals().update({"@type": Field("DVDFormat", const=True)})


DVDFormat.update_forward_refs()
