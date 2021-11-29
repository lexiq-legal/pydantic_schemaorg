from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Beach(CivicStructure):
    """Beach.

    See https://schema.org/Beach.

    """

    locals().update({"@type": Field("Beach", const=True)})


Beach.update_forward_refs()
