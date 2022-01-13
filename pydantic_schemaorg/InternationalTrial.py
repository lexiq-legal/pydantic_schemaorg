from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class InternationalTrial(MedicalTrialDesign):
    """An international trial.

    See: https://schema.org/InternationalTrial
    Model depth: 6
    """

    type_: str = Field("InternationalTrial", const=True, alias="@type")


if TYPE_CHECKING:

    InternationalTrial.update_forward_refs()
