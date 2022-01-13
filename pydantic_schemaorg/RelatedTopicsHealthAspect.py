from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class RelatedTopicsHealthAspect(HealthAspectEnumeration):
    """Other prominent or relevant topics tied to the main topic.

    See: https://schema.org/RelatedTopicsHealthAspect
    Model depth: 5
    """

    type_: str = Field("RelatedTopicsHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    RelatedTopicsHealthAspect.update_forward_refs()
