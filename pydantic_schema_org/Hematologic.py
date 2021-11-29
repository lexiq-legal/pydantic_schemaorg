from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Hematologic(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of blood and blood producing organs.

    See https://schema.org/Hematologic.

    """

    locals().update({"@type": Field("Hematologic", const=True)})


Hematologic.update_forward_refs()
