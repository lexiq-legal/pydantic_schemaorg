from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Museum(CivicStructure):
    """A museum.

    See https://schema.org/Museum.

    """

    locals().update({"@type": Field("Museum", const=True)})


Museum.update_forward_refs()
