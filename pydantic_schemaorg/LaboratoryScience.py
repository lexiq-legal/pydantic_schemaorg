from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class LaboratoryScience(MedicalSpecialty):
    """A medical science pertaining to chemical, hematological, immunologic, microscopic,"
     "or bacteriological diagnostic analyses or research.

    See: https://schema.org/LaboratoryScience
    Model depth: 6
    """

    type_: str = Field("LaboratoryScience", const=True, alias="@type")


if TYPE_CHECKING:

    LaboratoryScience.update_forward_refs()
