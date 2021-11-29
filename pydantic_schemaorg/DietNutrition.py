from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class DietNutrition(MedicalSpecialty, MedicalBusiness):
    """Dietetic and nutrition as a medical specialty.

    See https://schema.org/DietNutrition.

    """

    locals().update({"@type": Field("DietNutrition", const=True)})


DietNutrition.update_forward_refs()
