from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TravelAgency(LocalBusiness):
    """A travel agency.

    See https://schema.org/TravelAgency.

    """
    type_: str = Field("TravelAgency", const=True, alias='@type')
    

TravelAgency.update_forward_refs()
