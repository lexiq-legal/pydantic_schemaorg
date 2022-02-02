from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalProcedureType(MedicalEnumeration):
    """An enumeration that describes different types of medical procedures.

    See: https://schema.org/MedicalProcedureType
    Model depth: 5
    """
    type_: str = Field("MedicalProcedureType", alias='@type')
    

