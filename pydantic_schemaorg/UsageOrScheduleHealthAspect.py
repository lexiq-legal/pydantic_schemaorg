from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class UsageOrScheduleHealthAspect(HealthAspectEnumeration):
    """Content about how, when, frequency and dosage of a topic.

    See: https://schema.org/UsageOrScheduleHealthAspect
    Model depth: 5
    """

    type_: str = Field("UsageOrScheduleHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    UsageOrScheduleHealthAspect.update_forward_refs()
