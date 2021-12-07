from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Surgical(MedicalSpecialty):
    """A specific branch of medical science that pertains to treating diseases, injuries and"
     "deformities by manual and instrumental means.

    See https://schema.org/Surgical.

    """
    type_: str = Field("Surgical", const=True, alias='@type')
    

Surgical.update_forward_refs()
