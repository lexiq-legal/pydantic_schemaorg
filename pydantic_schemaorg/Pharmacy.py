from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Pharmacy(MedicalBusiness, MedicalOrganization):
    """A pharmacy or drugstore.

    See: https://schema.org/Pharmacy
    Model depth: 4
    """
    type_: str = Field("Pharmacy", alias='@type')
    

