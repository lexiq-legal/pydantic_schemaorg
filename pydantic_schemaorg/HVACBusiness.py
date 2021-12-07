from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provide Heating, Ventilation and Air Conditioning services.

    See https://schema.org/HVACBusiness.

    """
    type_: str = Field("HVACBusiness", const=True, alias='@type')
    

HVACBusiness.update_forward_refs()
