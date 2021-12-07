from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Podiatric(MedicalBusiness, MedicalSpecialty):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot"
     "disorders.

    See https://schema.org/Podiatric.

    """
    type_: str = Field("Podiatric", const=True, alias='@type')
    

Podiatric.update_forward_refs()
