from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class AmpStory(CreativeWork):
    """A creative work with a visual storytelling format intended to be viewed online, particularly"
     "on mobile devices.

    See https://schema.org/AmpStory.

    """

    locals().update({"@type": Field("AmpStory", const=True)})


AmpStory.update_forward_refs()
