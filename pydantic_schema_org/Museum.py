from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class Museum(CivicStructure):
    """A museum.

    See https://schema.org/Museum.

    """

    locals().update({"@type": Field("Museum", const=True)})


Museum.update_forward_refs()
