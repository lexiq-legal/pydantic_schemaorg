from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalTrialDesign(MedicalEnumeration):
    """Design models for medical trials. Enumerated type.

    See https://schema.org/MedicalTrialDesign.

    """
    type_: str = Field("MedicalTrialDesign", const=True, alias='@type')
    

MedicalTrialDesign.update_forward_refs()
