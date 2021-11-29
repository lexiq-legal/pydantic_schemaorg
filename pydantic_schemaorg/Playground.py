from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Playground(CivicStructure):
    """A playground.

    See https://schema.org/Playground.

    """

    locals().update({"@type": Field("Playground", const=True)})


Playground.update_forward_refs()
