from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision.

    See: https://schema.org/Optician
    Model depth: 5
    """
    type_: str = Field(default="Optician", alias='@type', const=True)
    
