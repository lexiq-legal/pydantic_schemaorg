from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Store import Store


class PawnShop(Store):
    """A shop that will buy, or lend money against the security of, personal possessions.

    See: https://schema.org/PawnShop
    Model depth: 5
    """
    type_: str = Field("PawnShop", alias='@type')
    

