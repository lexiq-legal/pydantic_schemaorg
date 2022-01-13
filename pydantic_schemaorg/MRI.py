from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class MRI(MedicalImagingTechnique):
    """Magnetic resonance imaging.

    See: https://schema.org/MRI
    Model depth: 6
    """

    type_: str = Field("MRI", const=True, alias="@type")


if TYPE_CHECKING:

    MRI.update_forward_refs()
