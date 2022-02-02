from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """A component of the human body circulatory system comprised of an intricate network of"
     "hollow tubes that transport blood throughout the entire body.

    See: https://schema.org/Vessel
    Model depth: 4
    """
    type_: str = Field("Vessel", alias='@type')
    

