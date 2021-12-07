from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Rheumatologic(MedicalSpecialty):
    """A specific branch of medical science that deals with the study and treatment of rheumatic,"
     "autoimmune or joint diseases.

    See https://schema.org/Rheumatologic.

    """
    type_: str = Field("Rheumatologic", const=True, alias='@type')
    

Rheumatologic.update_forward_refs()
