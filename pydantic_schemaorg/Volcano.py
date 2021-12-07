from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Volcano(Landform):
    """A volcano, like Fuji san.

    See https://schema.org/Volcano.

    """
    type_: str = Field("Volcano", const=True, alias='@type')
    

Volcano.update_forward_refs()
