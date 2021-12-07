from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class DietNutrition(MedicalBusiness, MedicalSpecialty):
    """Dietetic and nutrition as a medical specialty.

    See https://schema.org/DietNutrition.

    """
    type_: str = Field("DietNutrition", const=True, alias='@type')
    

DietNutrition.update_forward_refs()
