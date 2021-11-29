from pydantic import Field
from pydantic_schema_org.Specialty import Specialty
from pydantic_schema_org.MedicalEnumeration import MedicalEnumeration


class MedicalSpecialty(Specialty, MedicalEnumeration):
    """Any specific branch of medical science or practice. Medical specialities include clinical"
     "specialties that pertain to particular organ systems and their respective disease"
     "states, as well as allied health specialties. Enumerated type.

    See https://schema.org/MedicalSpecialty.

    """

    locals().update({"@type": Field("MedicalSpecialty", const=True)})


MedicalSpecialty.update_forward_refs()
