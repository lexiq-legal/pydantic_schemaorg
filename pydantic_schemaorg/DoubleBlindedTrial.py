from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class DoubleBlindedTrial(MedicalTrialDesign):
    """A trial design in which neither the researcher nor the patient knows the details of the"
     "treatment the patient was randomly assigned to.

    See: https://schema.org/DoubleBlindedTrial
    Model depth: 6
    """

    type_: str = Field("DoubleBlindedTrial", const=True, alias="@type")


if TYPE_CHECKING:

    DoubleBlindedTrial.update_forward_refs()
