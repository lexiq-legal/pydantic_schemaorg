from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Genetic(MedicalSpecialty):
    """A specific branch of medical science that pertains to hereditary transmission and the"
     "variation of inherited characteristics and disorders.

    See https://schema.org/Genetic.

    """
    type_: str = Field("Genetic", const=True, alias='@type')
    

Genetic.update_forward_refs()
