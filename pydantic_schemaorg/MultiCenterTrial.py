from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class MultiCenterTrial(MedicalTrialDesign):
    """A trial that takes place at multiple centers.

    See: https://schema.org/MultiCenterTrial
    Model depth: 6
    """

    type_: str = Field("MultiCenterTrial", const=True, alias="@type")


if TYPE_CHECKING:

    MultiCenterTrial.update_forward_refs()
