from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    See https://schema.org/TattooParlor.

    """
    type_: str = Field("TattooParlor", const=True, alias='@type')
    

TattooParlor.update_forward_refs()
