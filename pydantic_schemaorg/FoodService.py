from pydantic import Field
from pydantic_schemaorg.Service import Service


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner.

    See https://schema.org/FoodService.

    """

    locals().update({"@type": Field("FoodService", const=True)})


FoodService.update_forward_refs()
