from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class ContagiousnessHealthAspect(HealthAspectEnumeration):
    """Content about contagion mechanisms and contagiousness information over the topic.

    See: https://schema.org/ContagiousnessHealthAspect
    Model depth: 5
    """

    type_: str = Field("ContagiousnessHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    ContagiousnessHealthAspect.update_forward_refs()
