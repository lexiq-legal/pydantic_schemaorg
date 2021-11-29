from pydantic import Field
from pydantic_schema_org.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See https://schema.org/HealthAndBeautyBusiness.

    """

    locals().update({"@type": Field("HealthAndBeautyBusiness", const=True)})


HealthAndBeautyBusiness.update_forward_refs()
