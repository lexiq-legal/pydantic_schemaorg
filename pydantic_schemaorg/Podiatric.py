from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Podiatric(MedicalSpecialty, MedicalBusiness):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot"
     "disorders.

    See: https://schema.org/Podiatric
    Model depth: 5
    """

    type_: str = Field("Podiatric", const=True, alias="@type")


if TYPE_CHECKING:

    Podiatric.update_forward_refs()
