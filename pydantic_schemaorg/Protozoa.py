from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Protozoa(InfectiousAgentClass):
    """Single-celled organism that causes an infection.

    See: https://schema.org/Protozoa
    Model depth: 6
    """
    type_: str = Field("Protozoa", alias='@type')
    

