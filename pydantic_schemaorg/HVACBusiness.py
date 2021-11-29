from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provide Heating, Ventilation and Air Conditioning services.

    See https://schema.org/HVACBusiness.

    """

    locals().update({"@type": Field("HVACBusiness", const=True)})


HVACBusiness.update_forward_refs()
