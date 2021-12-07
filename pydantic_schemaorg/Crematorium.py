from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Crematorium(CivicStructure):
    """A crematorium.

    See https://schema.org/Crematorium.

    """
    type_: str = Field("Crematorium", const=True, alias='@type')
    

Crematorium.update_forward_refs()
