from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pediatric(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that specializes in the care of infants, children"
     "and adolescents.

    See https://schema.org/Pediatric.

    """
    type_: str = Field("Pediatric", const=True, alias='@type')
    

Pediatric.update_forward_refs()
