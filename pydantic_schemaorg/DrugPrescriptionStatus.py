from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class DrugPrescriptionStatus(MedicalEnumeration):
    """Indicates whether this drug is available by prescription or over-the-counter.

    See https://schema.org/DrugPrescriptionStatus.

    """

    locals().update({"@type": Field("DrugPrescriptionStatus", const=True)})


DrugPrescriptionStatus.update_forward_refs()
