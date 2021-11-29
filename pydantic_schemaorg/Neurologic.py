from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Neurologic(MedicalSpecialty):
    """A specific branch of medical science that studies the nerves and nervous system and its"
     "respective disease states.

    See https://schema.org/Neurologic.

    """

    locals().update({"@type": Field("Neurologic", const=True)})


Neurologic.update_forward_refs()
