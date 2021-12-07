from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class ShortStory(CreativeWork):
    """Short story or tale. A brief work of literature, usually written in narrative prose.

    See https://schema.org/ShortStory.

    """
    type_: str = Field("ShortStory", const=True, alias='@type')
    

ShortStory.update_forward_refs()
