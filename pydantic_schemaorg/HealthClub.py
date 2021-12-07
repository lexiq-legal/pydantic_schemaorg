from pydantic import Field
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HealthClub(SportsActivityLocation, HealthAndBeautyBusiness):
    """A health club.

    See https://schema.org/HealthClub.

    """
    type_: str = Field("HealthClub", const=True, alias='@type')
    

HealthClub.update_forward_refs()
