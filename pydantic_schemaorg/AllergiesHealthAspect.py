from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class AllergiesHealthAspect(HealthAspectEnumeration):
    """Content about the allergy-related aspects of a health topic.

    See: https://schema.org/AllergiesHealthAspect
    Model depth: 5
    """

    type_: str = Field("AllergiesHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    AllergiesHealthAspect.update_forward_refs()
