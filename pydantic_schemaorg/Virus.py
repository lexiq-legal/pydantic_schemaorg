from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Virus(InfectiousAgentClass):
    """Pathogenic virus that causes viral infection.

    See https://schema.org/Virus.

    """
    type_: str = Field("Virus", const=True, alias='@type')
    

Virus.update_forward_refs()
