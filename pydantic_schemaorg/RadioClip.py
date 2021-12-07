from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class RadioClip(Clip):
    """A short radio program or a segment/part of a radio program.

    See https://schema.org/RadioClip.

    """
    type_: str = Field("RadioClip", const=True, alias='@type')
    

RadioClip.update_forward_refs()
