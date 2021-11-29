from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium.

    See https://schema.org/Aquarium.

    """

    locals().update({"@type": Field("Aquarium", const=True)})


Aquarium.update_forward_refs()
