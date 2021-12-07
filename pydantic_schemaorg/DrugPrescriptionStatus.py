from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """Indicates whether this drug is available by prescription or over-the-counter.

    See https://schema.org/DrugPrescriptionStatus.

    """
    type_: str = Field("DrugPrescriptionStatus", const=True, alias='@type')
    

DrugPrescriptionStatus.update_forward_refs()
