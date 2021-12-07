from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class AmpStory(CreativeWork):
    """A creative work with a visual storytelling format intended to be viewed online, particularly"
     "on mobile devices.

    See https://schema.org/AmpStory.

    """
    type_: str = Field("AmpStory", const=True, alias='@type')
    

AmpStory.update_forward_refs()
