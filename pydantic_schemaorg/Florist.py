from pydantic import Field
from pydantic_schemaorg.Store import Store


class Florist(Store):
    """A florist.

    See https://schema.org/Florist.

    """
    type_: str = Field("Florist", const=True, alias='@type')
    

Florist.update_forward_refs()
