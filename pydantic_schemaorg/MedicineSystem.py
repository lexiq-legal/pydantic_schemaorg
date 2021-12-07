from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicineSystem(MedicalEnumeration):
    """Systems of medical practice.

    See https://schema.org/MedicineSystem.

    """
    type_: str = Field("MedicineSystem", const=True, alias='@type')
    

MedicineSystem.update_forward_refs()
