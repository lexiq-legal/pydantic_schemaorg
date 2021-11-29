from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """Beauty salon.

    See https://schema.org/BeautySalon.

    """

    locals().update({"@type": Field("BeautySalon", const=True)})


BeautySalon.update_forward_refs()
