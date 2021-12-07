from pydantic import Field
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class NoninvasiveProcedure(MedicalProcedureType):
    """A type of medical procedure that involves noninvasive techniques.

    See https://schema.org/NoninvasiveProcedure.

    """
    type_: str = Field("NoninvasiveProcedure", const=True, alias='@type')
    

NoninvasiveProcedure.update_forward_refs()
