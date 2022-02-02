from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class NoninvasiveProcedure(MedicalProcedureType):
    """A type of medical procedure that involves noninvasive techniques.

    See: https://schema.org/NoninvasiveProcedure
    Model depth: 6
    """
    type_: str = Field("NoninvasiveProcedure", alias='@type')
    

