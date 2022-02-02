from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class PublicSwimmingPool(SportsActivityLocation):
    """A public swimming pool.

    See: https://schema.org/PublicSwimmingPool
    Model depth: 5
    """
    type_: str = Field("PublicSwimmingPool", alias='@type')
    

