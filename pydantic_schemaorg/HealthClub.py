from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness
from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club.

    See https://schema.org/HealthClub.

    """

    locals().update({"@type": Field("HealthClub", const=True)})


HealthClub.update_forward_refs()
