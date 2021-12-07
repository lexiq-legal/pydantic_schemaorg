from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """A high school.

    See https://schema.org/HighSchool.

    """
    type_: str = Field("HighSchool", const=True, alias='@type')
    

HighSchool.update_forward_refs()
