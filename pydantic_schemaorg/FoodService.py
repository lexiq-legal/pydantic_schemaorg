from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Service import Service


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner.

    See: https://schema.org/FoodService
    Model depth: 4
    """
    type_: str = Field("FoodService", alias='@type')
    

