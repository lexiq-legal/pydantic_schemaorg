from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalGuideline import MedicalGuideline


class MedicalGuidelineContraindication(MedicalGuideline):
    """A guideline contraindication that designates a process as harmful and where quality"
     "of the data supporting the contraindication is sound.

    See: https://schema.org/MedicalGuidelineContraindication
    Model depth: 4
    """

    type_: str = Field("MedicalGuidelineContraindication", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalGuidelineContraindication.update_forward_refs()
