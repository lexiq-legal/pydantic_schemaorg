from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels.

    See https://schema.org/BoatTerminal.

    """

    locals().update({"@type": Field("BoatTerminal", const=True)})


BoatTerminal.update_forward_refs()
