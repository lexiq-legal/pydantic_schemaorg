from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Ligament(AnatomicalStructure):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect"
     "multiple bones, cartilages, and structurally support joints.

    See: https://schema.org/Ligament
    Model depth: 4
    """
    type_: str = Field("Ligament", alias='@type')
    

