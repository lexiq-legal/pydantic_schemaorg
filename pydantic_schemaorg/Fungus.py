from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Fungus(InfectiousAgentClass):
    """Pathogenic fungus.

    See https://schema.org/Fungus.

    """
    type_: str = Field("Fungus", const=True, alias='@type')
    

Fungus.update_forward_refs()
