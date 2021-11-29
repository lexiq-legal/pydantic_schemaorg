from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class MiddleSchool(EducationalOrganization):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    See https://schema.org/MiddleSchool.

    """

    locals().update({"@type": Field("MiddleSchool", const=True)})


MiddleSchool.update_forward_refs()
