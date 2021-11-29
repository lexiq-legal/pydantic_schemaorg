from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.Specialty import Specialty


class MedicalSpecialty(MedicalEnumeration, Specialty):
    """Any specific branch of medical science or practice. Medical specialities include clinical"
     "specialties that pertain to particular organ systems and their respective disease"
     "states, as well as allied health specialties. Enumerated type.

    See https://schema.org/MedicalSpecialty.

    """

    locals().update({"@type": Field("MedicalSpecialty", const=True)})


MedicalSpecialty.update_forward_refs()
