from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalStudyStatus(MedicalEnumeration):
    """The status of a medical study. Enumerated type.

    See: https://schema.org/MedicalStudyStatus
    Model depth: 5
    """
    type_: str = Field("MedicalStudyStatus", alias='@type')
    

