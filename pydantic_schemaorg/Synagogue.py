from pydantic import Field
from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue.

    See https://schema.org/Synagogue.

    """
    type_: str = Field("Synagogue", const=True, alias='@type')
    

Synagogue.update_forward_refs()
