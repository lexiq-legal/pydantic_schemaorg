from pydantic import Field
from pydantic_schemaorg.Service import Service


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner.

    See https://schema.org/FoodService.

    """
    type_: str = Field("FoodService", const=True, alias='@type')
    

FoodService.update_forward_refs()
