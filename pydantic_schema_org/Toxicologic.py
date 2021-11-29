from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty


class Toxicologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with poisons, their nature, effects"
     "and detection and involved in the treatment of poisoning.

    See https://schema.org/Toxicologic.

    """

    locals().update({"@type": Field("Toxicologic", const=True)})


Toxicologic.update_forward_refs()
