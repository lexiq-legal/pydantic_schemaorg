from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class VideoGameClip(Clip):
    """A short segment/part of a video game.

    See https://schema.org/VideoGameClip.

    """
    type_: str = Field("VideoGameClip", const=True, alias='@type')
    

VideoGameClip.update_forward_refs()
