from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Infectious(MedicalSpecialty):
    """Something in medical science that pertains to infectious diseases i.e caused by bacterial,"
     "viral, fungal or parasitic infections.

    See https://schema.org/Infectious.

    """
    type_: str = Field("Infectious", const=True, alias='@type')
    

Infectious.update_forward_refs()
