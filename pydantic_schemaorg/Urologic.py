from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Urologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the diagnosis and treatment"
     "of diseases pertaining to the urinary tract and the urogenital system.

    See https://schema.org/Urologic.

    """

    locals().update({"@type": Field("Urologic", const=True)})


Urologic.update_forward_refs()
