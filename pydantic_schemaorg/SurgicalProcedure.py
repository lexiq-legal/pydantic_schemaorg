from pydantic import Field
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class SurgicalProcedure(MedicalProcedure):
    """A medical procedure involving an incision with instruments; performed for diagnose,"
     "or therapeutic purposes.

    See https://schema.org/SurgicalProcedure.

    """
    type_: str = Field("SurgicalProcedure", const=True, alias='@type')
    

SurgicalProcedure.update_forward_refs()
