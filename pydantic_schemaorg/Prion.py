from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Prion(InfectiousAgentClass):
    """A prion is an infectious agent composed of protein in a misfolded form.

    See: https://schema.org/Prion
    Model depth: 6
    """
    type_: str = Field("Prion", alias='@type')
    

