from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class PhysicalTherapy(MedicalTherapy):
    """A process of progressive physical care and rehabilitation aimed at improving a health"
     "condition.

    See https://schema.org/PhysicalTherapy.

    """
    type_: str = Field("PhysicalTherapy", const=True, alias='@type')
    

PhysicalTherapy.update_forward_refs()
