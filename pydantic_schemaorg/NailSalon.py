from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    See https://schema.org/NailSalon.

    """
    type_: str = Field("NailSalon", const=True, alias='@type')
    

NailSalon.update_forward_refs()
