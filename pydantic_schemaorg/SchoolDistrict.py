from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


class SchoolDistrict(AdministrativeArea):
    """A School District is an administrative area for the administration of schools.

    See: https://schema.org/SchoolDistrict
    Model depth: 4
    """
    type_: str = Field("SchoolDistrict", alias='@type')
    

