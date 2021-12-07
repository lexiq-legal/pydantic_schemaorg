from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class MusicVideoObject(MediaObject):
    """A music video file.

    See https://schema.org/MusicVideoObject.

    """
    type_: str = Field("MusicVideoObject", const=True, alias='@type')
    

MusicVideoObject.update_forward_refs()
