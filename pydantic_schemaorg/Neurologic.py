from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Neurologic(MedicalSpecialty):
    """A specific branch of medical science that studies the nerves and nervous system and its"
     "respective disease states.

    See https://schema.org/Neurologic.

    """
    type_: str = Field("Neurologic", const=True, alias='@type')
    

Neurologic.update_forward_refs()
