from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalIndication import MedicalIndication


class TreatmentIndication(MedicalIndication):
    """An indication for treating an underlying condition, symptom, etc.

    See: https://schema.org/TreatmentIndication
    Model depth: 4
    """

    type_: str = Field("TreatmentIndication", const=True, alias="@type")


if TYPE_CHECKING:

    TreatmentIndication.update_forward_refs()
