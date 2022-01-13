from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SymptomsHealthAspect(HealthAspectEnumeration):
    """Symptoms or related symptoms of a Topic.

    See: https://schema.org/SymptomsHealthAspect
    Model depth: 5
    """

    type_: str = Field("SymptomsHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    SymptomsHealthAspect.update_forward_refs()
