from pydantic import Field
from pydantic_schema_org.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    See https://schema.org/TattooParlor.

    """

    locals().update({"@type": Field("TattooParlor", const=True)})


TattooParlor.update_forward_refs()
