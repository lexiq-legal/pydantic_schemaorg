from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class Specialty(Enumeration):
    """Any branch of a field in which people typically develop specific expertise, usually"
     "after significant study, time, and effort.

    See: https://schema.org/Specialty
    Model depth: 4
    """
    type_: str = Field("Specialty", alias='@type')
    

