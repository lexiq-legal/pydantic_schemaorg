from pydantic import Field
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class PercutaneousProcedure(MedicalProcedureType):
    """A type of medical procedure that involves percutaneous techniques, where access to"
     "organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based"
     "procedures like stent delivery.

    See https://schema.org/PercutaneousProcedure.

    """
    type_: str = Field("PercutaneousProcedure", const=True, alias='@type')
    

PercutaneousProcedure.update_forward_refs()
