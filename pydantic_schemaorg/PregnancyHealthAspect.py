from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PregnancyHealthAspect(HealthAspectEnumeration):
    """Content discussing pregnancy-related aspects of a health topic.

    See: https://schema.org/PregnancyHealthAspect
    Model depth: 5
    """

    type_: str = Field("PregnancyHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    PregnancyHealthAspect.update_forward_refs()
