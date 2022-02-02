from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MedicalEnumeration(Enumeration):
    """Enumerations related to health and the practice of medicine: A concept that is used to"
     "attribute a quality to another concept, as a qualifier, a collection of items or a listing"
     "of all of the elements of a set in medicine practice.

    See: https://schema.org/MedicalEnumeration
    Model depth: 4
    """
    type_: str = Field("MedicalEnumeration", alias='@type')
    

