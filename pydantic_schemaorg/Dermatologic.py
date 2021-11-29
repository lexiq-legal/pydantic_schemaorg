from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dermatologic(MedicalSpecialty):
    """Something relating to or practicing dermatology.

    See https://schema.org/Dermatologic.

    """

    locals().update({"@type": Field("Dermatologic", const=True)})


Dermatologic.update_forward_refs()
