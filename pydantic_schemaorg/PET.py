from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class PET(MedicalImagingTechnique):
    """Positron emission tomography imaging.

    See: https://schema.org/PET
    Model depth: 6
    """

    type_: str = Field("PET", const=True, alias="@type")


if TYPE_CHECKING:

    PET.update_forward_refs()
