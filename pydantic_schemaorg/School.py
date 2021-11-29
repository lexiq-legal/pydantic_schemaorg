from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class School(EducationalOrganization):
    """A school.

    See https://schema.org/School.

    """

    locals().update({"@type": Field("School", const=True)})


School.update_forward_refs()
