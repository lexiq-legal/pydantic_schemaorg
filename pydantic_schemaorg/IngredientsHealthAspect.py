from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class IngredientsHealthAspect(HealthAspectEnumeration):
    """Content discussing ingredients-related aspects of a health topic.

    See: https://schema.org/IngredientsHealthAspect
    Model depth: 5
    """

    type_: str = Field("IngredientsHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    IngredientsHealthAspect.update_forward_refs()
