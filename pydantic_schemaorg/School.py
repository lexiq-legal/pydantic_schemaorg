from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class School(EducationalOrganization):
    """A school.

    See: https://schema.org/School
    Model depth: 4
    """
    type_: str = Field("School", alias='@type')
    

