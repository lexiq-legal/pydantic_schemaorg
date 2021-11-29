from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Cardiovascular(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of heart and vasculature.

    See https://schema.org/Cardiovascular.

    """

    locals().update({"@type": Field("Cardiovascular", const=True)})


Cardiovascular.update_forward_refs()
