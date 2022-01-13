from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalIndication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """An indication for preventing an underlying condition, symptom, etc.

    See: https://schema.org/PreventionIndication
    Model depth: 4
    """

    type_: str = Field("PreventionIndication", const=True, alias="@type")


if TYPE_CHECKING:

    PreventionIndication.update_forward_refs()
