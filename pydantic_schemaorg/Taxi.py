from pydantic import Field
from pydantic_schemaorg.Service import Service


class Taxi(Service):
    """A taxi.

    See https://schema.org/Taxi.

    """
    type_: str = Field("Taxi", const=True, alias='@type')
    

Taxi.update_forward_refs()
