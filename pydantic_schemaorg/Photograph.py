from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Photograph(CreativeWork):
    """A photograph.

    See https://schema.org/Photograph.

    """
    type_: str = Field("Photograph", const=True, alias='@type')
    

Photograph.update_forward_refs()
