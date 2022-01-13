from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemMetric(SizeSystemEnumeration):
    """Metric size system.

    See: https://schema.org/SizeSystemMetric
    Model depth: 5
    """

    type_: str = Field("SizeSystemMetric", const=True, alias="@type")


if TYPE_CHECKING:

    SizeSystemMetric.update_forward_refs()
