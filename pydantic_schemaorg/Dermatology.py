from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatology(MedicalBusiness, MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of skin.

    See https://schema.org/Dermatology.

    """

    locals().update({"@type": Field("Dermatology", const=True)})


Dermatology.update_forward_refs()
