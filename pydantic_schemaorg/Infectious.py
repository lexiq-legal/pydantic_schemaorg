from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Infectious(MedicalSpecialty):
    """Something in medical science that pertains to infectious diseases i.e caused by bacterial,"
     "viral, fungal or parasitic infections.

    See https://schema.org/Infectious.

    """

    locals().update({"@type": Field("Infectious", const=True)})


Infectious.update_forward_refs()
