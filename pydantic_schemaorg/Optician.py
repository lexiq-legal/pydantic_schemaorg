from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Optician(MedicalBusiness):
    """A store that sells reading glasses and similar devices for improving vision.

    See https://schema.org/Optician.

    """
    type_: str = Field("Optician", const=True, alias='@type')
    

Optician.update_forward_refs()
