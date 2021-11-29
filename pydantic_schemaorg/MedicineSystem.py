from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """Systems of medical practice.

    See https://schema.org/MedicineSystem.

    """

    locals().update({"@type": Field("MedicineSystem", const=True)})


MedicineSystem.update_forward_refs()
