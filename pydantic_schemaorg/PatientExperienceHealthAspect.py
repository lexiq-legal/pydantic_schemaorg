from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PatientExperienceHealthAspect(HealthAspectEnumeration):
    """Content about the real life experience of patients or people that have lived a similar"
     "experience about the topic. May be forums, topics, Q-and-A and related material.

    See: https://schema.org/PatientExperienceHealthAspect
    Model depth: 5
    """

    type_: str = Field("PatientExperienceHealthAspect", const=True, alias="@type")


if TYPE_CHECKING:

    PatientExperienceHealthAspect.update_forward_refs()
