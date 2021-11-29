from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class PatientExperienceHealthAspect(HealthAspectEnumeration):
    """Content about the real life experience of patients or people that have lived a similar"
     "experience about the topic. May be forums, topics, Q-and-A and related material.

    See https://schema.org/PatientExperienceHealthAspect.

    """

    locals().update({"@type": Field("PatientExperienceHealthAspect", const=True)})


PatientExperienceHealthAspect.update_forward_refs()
