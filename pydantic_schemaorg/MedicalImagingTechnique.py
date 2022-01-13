from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalImagingTechnique(MedicalEnumeration):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    See: https://schema.org/MedicalImagingTechnique
    Model depth: 5
    """

    type_: str = Field("MedicalImagingTechnique", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalImagingTechnique.update_forward_refs()
