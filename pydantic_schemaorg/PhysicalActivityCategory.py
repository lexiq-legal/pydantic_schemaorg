from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class PhysicalActivityCategory(Enumeration):
    """Categories of physical activity, organized by physiologic classification.

    See: https://schema.org/PhysicalActivityCategory
    Model depth: 4
    """

    type_: str = Field("PhysicalActivityCategory", const=True, alias="@type")


if TYPE_CHECKING:

    PhysicalActivityCategory.update_forward_refs()
