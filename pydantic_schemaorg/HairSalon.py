from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """A hair salon.

    See https://schema.org/HairSalon.

    """

    locals().update({"@type": Field("HairSalon", const=True)})


HairSalon.update_forward_refs()
