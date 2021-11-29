from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Nursing(MedicalBusiness, MedicalSpecialty):
    """A health profession of a person formally educated and trained in the care of the sick or"
     "infirm person.

    See https://schema.org/Nursing.

    """

    locals().update({"@type": Field("Nursing", const=True)})


Nursing.update_forward_refs()
