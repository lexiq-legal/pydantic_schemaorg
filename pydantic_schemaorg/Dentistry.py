from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Dentistry(MedicalSpecialty):
    """A branch of medicine that is involved in the dental care.

    See https://schema.org/Dentistry.

    """

    locals().update({"@type": Field("Dentistry", const=True)})


Dentistry.update_forward_refs()
