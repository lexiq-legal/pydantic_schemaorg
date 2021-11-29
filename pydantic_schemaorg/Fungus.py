from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Fungus(InfectiousAgentClass):
    """Pathogenic fungus.

    See https://schema.org/Fungus.

    """

    locals().update({"@type": Field("Fungus", const=True)})


Fungus.update_forward_refs()
