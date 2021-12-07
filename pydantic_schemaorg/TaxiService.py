from pydantic import Field
from pydantic_schemaorg.Service import Service


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated"
     "based on distance traveled.

    See https://schema.org/TaxiService.

    """
    type_: str = Field("TaxiService", const=True, alias='@type')
    

TaxiService.update_forward_refs()
