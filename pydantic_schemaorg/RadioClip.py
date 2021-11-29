from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program.

    See https://schema.org/RadioClip.

    """

    locals().update({"@type": Field("RadioClip", const=True)})


RadioClip.update_forward_refs()
