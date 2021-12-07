from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    See https://schema.org/Continent.

    """
    type_: str = Field("Continent", const=True, alias='@type')
    

Continent.update_forward_refs()
