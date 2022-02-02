from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment withclinical examination.

    See: https://schema.org/CardiovascularExam
    Model depth: 5
    """
    type_: str = Field("CardiovascularExam", alias='@type')
    

