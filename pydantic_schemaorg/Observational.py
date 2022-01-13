from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalObservationalStudyDesign import (
    MedicalObservationalStudyDesign,
)


class Observational(MedicalObservationalStudyDesign):
    """An observational study design.

    See: https://schema.org/Observational
    Model depth: 6
    """

    type_: str = Field("Observational", const=True, alias="@type")


if TYPE_CHECKING:

    Observational.update_forward_refs()
