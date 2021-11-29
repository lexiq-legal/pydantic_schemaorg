from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See https://schema.org/HealthAndBeautyBusiness.

    """

    locals().update({"@type": Field("HealthAndBeautyBusiness", const=True)})


HealthAndBeautyBusiness.update_forward_refs()
