from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dentistry(MedicalSpecialty):
    """A branch of medicine that is involved in the dental care.

    See https://schema.org/Dentistry.

    """
    type_: str = Field("Dentistry", const=True, alias='@type')
    

Dentistry.update_forward_refs()
