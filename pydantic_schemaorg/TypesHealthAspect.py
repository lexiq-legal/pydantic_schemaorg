from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class TypesHealthAspect(HealthAspectEnumeration):
    """Categorization and other types related to a topic.

    See: https://schema.org/TypesHealthAspect
    Model depth: 5
    """

    type_: str = Field("TypesHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    TypesHealthAspect.update_forward_refs()
