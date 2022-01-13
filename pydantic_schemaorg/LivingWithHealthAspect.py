from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class LivingWithHealthAspect(HealthAspectEnumeration):
    """Information about coping or life related to the topic.

    See: https://schema.org/LivingWithHealthAspect
    Model depth: 5
    """

    type_: str = Field("LivingWithHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    LivingWithHealthAspect.update_forward_refs()
