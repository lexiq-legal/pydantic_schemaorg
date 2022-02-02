from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class Preschool(EducationalOrganization):
    """A preschool.

    See: https://schema.org/Preschool
    Model depth: 4
    """
    type_: str = Field("Preschool", alias='@type')
    

