from pydantic import Field
from pydantic_schema_org.EducationalOrganization import EducationalOrganization


class HighSchool(EducationalOrganization):
    """A high school.

    See https://schema.org/HighSchool.

    """

    locals().update({"@type": Field("HighSchool", const=True)})


HighSchool.update_forward_refs()
