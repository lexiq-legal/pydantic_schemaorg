from pydantic import Field
from pydantic_schema_org.MedicalEnumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """The status of a medical study. Enumerated type.

    See https://schema.org/MedicalStudyStatus.

    """

    locals().update({"@type": Field("MedicalStudyStatus", const=True)})


MedicalStudyStatus.update_forward_refs()
