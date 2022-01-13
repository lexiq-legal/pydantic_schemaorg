from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class MisconceptionsHealthAspect(HealthAspectEnumeration):
    """Content about common misconceptions and myths that are related to a topic.

    See: https://schema.org/MisconceptionsHealthAspect
    Model depth: 5
    """

    type_: str = Field("MisconceptionsHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    MisconceptionsHealthAspect.update_forward_refs()
