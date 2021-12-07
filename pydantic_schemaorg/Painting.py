from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Painting(CreativeWork):
    """A painting.

    See https://schema.org/Painting.

    """
    type_: str = Field("Painting", const=True, alias='@type')
    

Painting.update_forward_refs()
