from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Observational(MedicalObservationalStudyDesign):
    """An observational study design.

    See https://schema.org/Observational.

    """
    type_: str = Field("Observational", const=True, alias='@type')
    

Observational.update_forward_refs()
