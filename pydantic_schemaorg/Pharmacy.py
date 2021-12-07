from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See https://schema.org/Pharmacy.

    """
    type_: str = Field("Pharmacy", const=True, alias='@type')
    

Pharmacy.update_forward_refs()
