from pydantic import Field
from pydantic_schemaorg.Service import Service


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated"
     "based on distance traveled.

    See https://schema.org/TaxiService.

    """

    locals().update({"@type": Field("TaxiService", const=True)})


TaxiService.update_forward_refs()
