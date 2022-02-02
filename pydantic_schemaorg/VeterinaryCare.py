from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See: https://schema.org/VeterinaryCare
    Model depth: 4
    """
    type_: str = Field("VeterinaryCare", alias='@type')
    

