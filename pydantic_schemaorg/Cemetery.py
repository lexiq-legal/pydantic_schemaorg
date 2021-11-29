from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard.

    See https://schema.org/Cemetery.

    """

    locals().update({"@type": Field("Cemetery", const=True)})


Cemetery.update_forward_refs()
