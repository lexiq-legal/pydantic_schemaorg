from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class TouristInformationCenter(LocalBusiness):
    """A tourist information center.

    See https://schema.org/TouristInformationCenter.

    """
    type_: str = Field("TouristInformationCenter", const=True, alias='@type')
    

TouristInformationCenter.update_forward_refs()
