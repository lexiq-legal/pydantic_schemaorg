from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatologic(MedicalSpecialty):
    """Something relating to or practicing dermatology.

    See https://schema.org/Dermatologic.

    """
    type_: str = Field("Dermatologic", const=True, alias='@type')
    

Dermatologic.update_forward_refs()
