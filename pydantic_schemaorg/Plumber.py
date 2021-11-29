from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """A plumbing service.

    See https://schema.org/Plumber.

    """

    locals().update({"@type": Field("Plumber", const=True)})


Plumber.update_forward_refs()
