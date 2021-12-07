from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalObservationalStudyDesign(MedicalEnumeration):
    """Design models for observational medical studies. Enumerated type.

    See https://schema.org/MedicalObservationalStudyDesign.

    """
    type_: str = Field("MedicalObservationalStudyDesign", const=True, alias='@type')
    

MedicalObservationalStudyDesign.update_forward_refs()
