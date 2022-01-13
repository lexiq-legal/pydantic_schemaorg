from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class DietNutrition(MedicalSpecialty, MedicalBusiness):
    """Dietetic and nutrition as a medical specialty.

    See: https://schema.org/DietNutrition
    Model depth: 5
    """

    type_: str = Field("DietNutrition", const=True, alias="@type")


if TYPE_CHECKING:

    DietNutrition.update_forward_refs()
