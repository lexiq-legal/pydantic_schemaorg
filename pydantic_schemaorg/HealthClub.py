from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club.

    See https://schema.org/HealthClub.

    """
    type_: str = Field("HealthClub", const=True, alias='@type')
    

HealthClub.update_forward_refs()
