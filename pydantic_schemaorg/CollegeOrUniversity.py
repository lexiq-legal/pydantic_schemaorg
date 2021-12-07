from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    See https://schema.org/CollegeOrUniversity.

    """
    type_: str = Field("CollegeOrUniversity", const=True, alias='@type')
    

CollegeOrUniversity.update_forward_refs()
