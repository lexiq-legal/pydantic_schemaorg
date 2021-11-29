from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Endocrine(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of endocrine glands and their secretions.

    See https://schema.org/Endocrine.

    """

    locals().update({"@type": Field("Endocrine", const=True)})


Endocrine.update_forward_refs()
