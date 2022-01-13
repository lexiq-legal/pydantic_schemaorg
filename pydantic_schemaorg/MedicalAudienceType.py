from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalAudienceType(MedicalEnumeration):
    """Target audiences types for medical web pages. Enumerated type.

    See: https://schema.org/MedicalAudienceType
    Model depth: 5
    """

    type_: str = Field("MedicalAudienceType", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalAudienceType.update_forward_refs()
