from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Gastroenterologic(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of digestive system.

    See https://schema.org/Gastroenterologic.

    """

    locals().update({"@type": Field("Gastroenterologic", const=True)})


Gastroenterologic.update_forward_refs()
