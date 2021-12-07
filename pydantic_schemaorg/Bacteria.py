from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Bacteria(InfectiousAgentClass):
    """Pathogenic bacteria that cause bacterial infection.

    See https://schema.org/Bacteria.

    """
    type_: str = Field("Bacteria", const=True, alias='@type')
    

Bacteria.update_forward_refs()
