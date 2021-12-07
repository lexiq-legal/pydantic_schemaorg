from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Quantity(Intangible):
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass"
     "are entities like '3 Kg' or '4 milligrams'.

    See https://schema.org/Quantity.

    """
    type_: str = Field("Quantity", const=True, alias='@type')
    

Quantity.update_forward_refs()
