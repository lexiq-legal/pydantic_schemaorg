from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Sculpture(CreativeWork):
    """A piece of sculpture.

    See https://schema.org/Sculpture.

    """
    type_: str = Field("Sculpture", const=True, alias='@type')
    

Sculpture.update_forward_refs()
