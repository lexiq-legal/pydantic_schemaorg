from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PatientExperienceHealthAspect(HealthAspectEnumeration):
    """Content about the real life experience of patients or people that have lived a similar"
     "experience about the topic. May be forums, topics, Q-and-A and related material.

    See: https://schema.org/PatientExperienceHealthAspect
    Model depth: 5
    """
    type_: str = Field("PatientExperienceHealthAspect", alias='@type')
    

