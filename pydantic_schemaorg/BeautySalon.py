from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """Beauty salon.

    See https://schema.org/BeautySalon.

    """
    type_: str = Field("BeautySalon", const=True, alias='@type')
    

BeautySalon.update_forward_refs()
