from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalDevicePurpose(MedicalEnumeration):
    """Categories of medical devices, organized by the purpose or intended use of the device.

    See: https://schema.org/MedicalDevicePurpose
    Model depth: 5
    """

    type_: str = Field("MedicalDevicePurpose", const=True, alias="@type")


if TYPE_CHECKING:

    MedicalDevicePurpose.update_forward_refs()
