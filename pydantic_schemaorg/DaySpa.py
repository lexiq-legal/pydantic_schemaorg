from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """A day spa.

    See https://schema.org/DaySpa.

    """
    type_: str = Field("DaySpa", const=True, alias='@type')
    

DaySpa.update_forward_refs()
