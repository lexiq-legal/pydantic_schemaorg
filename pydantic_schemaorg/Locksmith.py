from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    See https://schema.org/Locksmith.

    """

    locals().update({"@type": Field("Locksmith", const=True)})


Locksmith.update_forward_refs()
