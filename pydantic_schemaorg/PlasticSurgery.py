from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class PlasticSurgery(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that pertains to therapeutic or cosmetic repair"
     "or re-formation of missing, injured or malformed tissues or body parts by manual and"
     "instrumental means.

    See https://schema.org/PlasticSurgery.

    """
    type_: str = Field("PlasticSurgery", const=True, alias='@type')
    

PlasticSurgery.update_forward_refs()
