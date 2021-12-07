from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Protozoa(InfectiousAgentClass):
    """Single-celled organism that causes an infection.

    See https://schema.org/Protozoa.

    """
    type_: str = Field("Protozoa", const=True, alias='@type')
    

Protozoa.update_forward_refs()
