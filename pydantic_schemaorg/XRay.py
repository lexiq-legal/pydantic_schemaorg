from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalImagingTechnique import MedicalImagingTechnique


class XRay(MedicalImagingTechnique):
    """X-ray imaging.

    See: https://schema.org/XRay
    Model depth: 6
    """

    type_: str = Field("XRay", const=True, alias="@type")


if TYPE_CHECKING:

    XRay.update_forward_refs()
