from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class EffectivenessHealthAspect(HealthAspectEnumeration):
    """Content about the effectiveness-related aspects of a health topic.

    See: https://schema.org/EffectivenessHealthAspect
    Model depth: 5
    """

    type_: str = Field("EffectivenessHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    EffectivenessHealthAspect.update_forward_refs()
