from pydantic import Field
from pydantic_schema_org.SportsActivityLocation import SportsActivityLocation
from pydantic_schema_org.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HealthClub(SportsActivityLocation, HealthAndBeautyBusiness):
    """A health club.

    See https://schema.org/HealthClub.

    """

    locals().update({"@type": Field("HealthClub", const=True)})


HealthClub.update_forward_refs()
