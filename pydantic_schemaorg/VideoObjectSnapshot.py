from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.VideoObject import VideoObject


class VideoObjectSnapshot(VideoObject):
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte"
     "identical files, for the purposes of this type, considered identical. If they have different"
     "embedded metadata the files will differ. Different external facts about the files,"
     "e.g. creator or dateCreated that aren't represented in their actual content, do not"
     "affect this notion of identity.

    See: https://schema.org/VideoObjectSnapshot
    Model depth: 5
    """
    type_: str = Field("VideoObjectSnapshot", alias='@type')
    

