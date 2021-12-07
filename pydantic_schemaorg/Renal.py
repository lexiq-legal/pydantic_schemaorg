from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Renal(MedicalSpecialty):
    """A specific branch of medical science that pertains to the study of the kidneys and its"
     "respective disease states.

    See https://schema.org/Renal.

    """
    type_: str = Field("Renal", const=True, alias='@type')
    

Renal.update_forward_refs()
