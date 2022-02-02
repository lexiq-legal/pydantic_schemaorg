from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic,"
     "purposes.

    See: https://schema.org/DiagnosticProcedure
    Model depth: 4
    """
    type_: str = Field("DiagnosticProcedure", alias='@type')
    

