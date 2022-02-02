from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class MulticellularParasite(InfectiousAgentClass):
    """Multicellular parasite that causes an infection.

    See: https://schema.org/MulticellularParasite
    Model depth: 6
    """
    type_: str = Field("MulticellularParasite", alias='@type')
    

