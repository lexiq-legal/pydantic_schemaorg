from pydantic import Field
from pydantic_schema_org.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    See https://schema.org/Electrician.

    """

    locals().update({"@type": Field("Electrician", const=True)})


Electrician.update_forward_refs()
