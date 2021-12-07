from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels.

    See https://schema.org/BoatTerminal.

    """
    type_: str = Field("BoatTerminal", const=True, alias='@type')
    

BoatTerminal.update_forward_refs()
