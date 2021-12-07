from pydantic import Field
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class DiagnosticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic,"
     "purposes.

    See https://schema.org/DiagnosticProcedure.

    """
    type_: str = Field("DiagnosticProcedure", const=True, alias='@type')
    

DiagnosticProcedure.update_forward_refs()
