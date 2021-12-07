from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque.

    See https://schema.org/Mosque.

    """
    type_: str = Field("Mosque", const=True, alias='@type')
    

Mosque.update_forward_refs()
