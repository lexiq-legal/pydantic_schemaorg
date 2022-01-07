from pydantic import Field
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class PalliativeProcedure(MedicalProcedure, MedicalTherapy):
    """A medical procedure intended primarily for palliative purposes, aimed at relieving"
     "the symptoms of an underlying health condition.

    See https://schema.org/PalliativeProcedure.

    """
    type_: str = Field("PalliativeProcedure", const=True, alias='@type')
    

PalliativeProcedure.update_forward_refs()
