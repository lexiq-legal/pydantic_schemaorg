from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.LocalBusiness import LocalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Dentist(MedicalBusiness, LocalBusiness, MedicalOrganization):
    """A dentist.

    See: https://schema.org/Dentist
    Model depth: 4
    """
    type_: str = Field("Dentist", alias='@type')
    

