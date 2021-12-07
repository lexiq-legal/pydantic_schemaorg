from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TelevisionStation(LocalBusiness):
    """A television station.

    See https://schema.org/TelevisionStation.

    """
    type_: str = Field("TelevisionStation", const=True, alias='@type')
    

TelevisionStation.update_forward_refs()
