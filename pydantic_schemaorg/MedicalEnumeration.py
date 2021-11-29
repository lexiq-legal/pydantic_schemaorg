from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MedicalEnumeration(Enumeration):
    """Enumerations related to health and the practice of medicine: A concept that is used to"
     "attribute a quality to another concept, as a qualifier, a collection of items or a listing"
     "of all of the elements of a set in medicine practice.

    See https://schema.org/MedicalEnumeration.

    """

    locals().update({"@type": Field("MedicalEnumeration", const=True)})


MedicalEnumeration.update_forward_refs()
