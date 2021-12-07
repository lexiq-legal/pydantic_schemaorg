from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Otolaryngologic(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that is concerned with the ear, nose and throat and"
     "their respective disease states.

    See https://schema.org/Otolaryngologic.

    """
    type_: str = Field("Otolaryngologic", const=True, alias='@type')
    

Otolaryngologic.update_forward_refs()
