from pydantic import Field
from pydantic_schemaorg.AudioObject import AudioObject


class AudioObjectSnapshot(AudioObject):
    """A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte"
     "identical files, for the purposes of this type, considered identical. If they have different"
     "embedded metadata the files will differ. Different external facts about the files,"
     "e.g. creator or dateCreated that aren't represented in their actual content, do not"
     "affect this notion of identity.

    See https://schema.org/AudioObjectSnapshot.

    """

    locals().update({"@type": Field("AudioObjectSnapshot", const=True)})


AudioObjectSnapshot.update_forward_refs()
