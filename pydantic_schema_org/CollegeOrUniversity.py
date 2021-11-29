from pydantic import Field
from pydantic_schema_org.EducationalOrganization import EducationalOrganization


class CollegeOrUniversity(EducationalOrganization):
    """A college, university, or other third-level educational institution.

    See https://schema.org/CollegeOrUniversity.

    """

    locals().update({"@type": Field("CollegeOrUniversity", const=True)})


CollegeOrUniversity.update_forward_refs()
