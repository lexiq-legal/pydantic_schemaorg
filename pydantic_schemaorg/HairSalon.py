from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """A hair salon.

    See https://schema.org/HairSalon.

    """
    type_: str = Field("HairSalon", const=True, alias='@type')
    

HairSalon.update_forward_refs()
