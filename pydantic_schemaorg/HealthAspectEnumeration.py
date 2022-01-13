from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class HealthAspectEnumeration(Enumeration):
    """HealthAspectEnumeration enumerates several aspects of health content online, each"
     "of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    See: https://schema.org/HealthAspectEnumeration
    Model depth: 4
    """

    type_: str = Field("HealthAspectEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    HealthAspectEnumeration.update_forward_refs()
