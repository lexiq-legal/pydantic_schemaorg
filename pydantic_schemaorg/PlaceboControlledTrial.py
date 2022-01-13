from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class PlaceboControlledTrial(MedicalTrialDesign):
    """A placebo-controlled trial design.

    See: https://schema.org/PlaceboControlledTrial
    Model depth: 6
    """

    type_: str = Field("PlaceboControlledTrial", const=True, alias="@type")


if TYPE_CHECKING:

    PlaceboControlledTrial.update_forward_refs()
