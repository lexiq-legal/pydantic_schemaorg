from pydantic import Field
from pydantic_schema_org.CivicStructure import CivicStructure


class Crematorium(CivicStructure):
    """A crematorium.

    See https://schema.org/Crematorium.

    """

    locals().update({"@type": Field("Crematorium", const=True)})


Crematorium.update_forward_refs()
