from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    See: https://schema.org/CollegeOrUniversity
    Model depth: 4
    """
    type_: str = Field("CollegeOrUniversity", alias='@type')
    

