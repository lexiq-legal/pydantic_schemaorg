from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Physiotherapy(MedicalBusiness, MedicalSpecialty):
    """The practice of treatment of disease, injury, or deformity by physical methods such"
     "as massage, heat treatment, and exercise rather than by drugs or surgery..

    See https://schema.org/Physiotherapy.

    """
    type_: str = Field("Physiotherapy", const=True, alias='@type')
    

Physiotherapy.update_forward_refs()
