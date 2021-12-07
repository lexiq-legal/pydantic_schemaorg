from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See https://schema.org/HealthAndBeautyBusiness.

    """
    type_: str = Field("HealthAndBeautyBusiness", const=True, alias='@type')
    

HealthAndBeautyBusiness.update_forward_refs()
