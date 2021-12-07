from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Gastroenterologic(MedicalSpecialty):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders"
     "of digestive system.

    See https://schema.org/Gastroenterologic.

    """
    type_: str = Field("Gastroenterologic", const=True, alias='@type')
    

Gastroenterologic.update_forward_refs()
