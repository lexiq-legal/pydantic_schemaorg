from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class OpenTrial(MedicalTrialDesign):
    """A trial design in which the researcher knows the full details of the treatment, and so"
     "does the patient.

    See: https://schema.org/OpenTrial
    Model depth: 6
    """

    type_: str = Field("OpenTrial", const=True, alias="@type")


if TYPE_CHECKING:

    OpenTrial.update_forward_refs()
