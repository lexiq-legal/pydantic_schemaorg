from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Dentist(MedicalBusiness, MedicalOrganization, LocalBusiness):
    """A dentist.

    See: https://schema.org/Dentist
    Model depth: 4
    """
    type_: str = Field("Dentist", alias='@type')
    

