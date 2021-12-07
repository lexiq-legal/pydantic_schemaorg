from pydantic import Field
from pydantic_schemaorg.Service import Service


class CableOrSatelliteService(Service):
    """A service which provides access to media programming like TV or radio. Access may be via"
     "cable or satellite.

    See https://schema.org/CableOrSatelliteService.

    """
    type_: str = Field("CableOrSatelliteService", const=True, alias='@type')
    

CableOrSatelliteService.update_forward_refs()
