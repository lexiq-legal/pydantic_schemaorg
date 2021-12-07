from pydantic import Field
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class VeterinaryCare(MedicalOrganization):
    """A vet's office.

    See https://schema.org/VeterinaryCare.

    """
    type_: str = Field("VeterinaryCare", const=True, alias='@type')
    

VeterinaryCare.update_forward_refs()
