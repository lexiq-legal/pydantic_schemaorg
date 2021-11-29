from pydantic import Field
from pydantic_schemaorg.Clip import Clip


class VideoGameClip(Clip):
    """A short segment/part of a video game.

    See https://schema.org/VideoGameClip.

    """

    locals().update({"@type": Field("VideoGameClip", const=True)})


VideoGameClip.update_forward_refs()
