from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ScreeningHealthAspect(HealthAspectEnumeration):
    """Content about how to screen or further filter a topic.

    See: https://schema.org/ScreeningHealthAspect
    Model depth: 5
    """

    type_: str = Field("ScreeningHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    ScreeningHealthAspect.update_forward_refs()
