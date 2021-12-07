from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class LaboratoryScience(MedicalSpecialty):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic,"
     "or bacteriological diagnostic analyses or research.

    See https://schema.org/LaboratoryScience.

    """
    type_: str = Field("LaboratoryScience", const=True, alias='@type')
    

LaboratoryScience.update_forward_refs()
