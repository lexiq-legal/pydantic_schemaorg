from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class Ultrasound(MedicalImagingTechnique):
    """Ultrasound imaging.

    See: https://schema.org/Ultrasound
    Model depth: 6
    """

    type_: str = Field("Ultrasound", const=True, alias="@type")


if TYPE_CHECKING:

    Ultrasound.update_forward_refs()
