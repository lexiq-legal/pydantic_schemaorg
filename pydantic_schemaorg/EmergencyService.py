from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class EmergencyService(LocalBusiness):
    """An emergency service, such as a fire station or ER.

    See: https://schema.org/EmergencyService
    Model depth: 4
    """
    type_: str = Field("EmergencyService", alias='@type')
    

