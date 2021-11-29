from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class MusicVideoObject(MediaObject):
    """A music video file.

    See https://schema.org/MusicVideoObject.

    """

    locals().update({"@type": Field("MusicVideoObject", const=True)})


MusicVideoObject.update_forward_refs()
