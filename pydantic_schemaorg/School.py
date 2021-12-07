from pydantic import Field
from pydantic_schemaorg.EducationalOrganization import EducationalOrganization


class School(EducationalOrganization):
    """A school.

    See https://schema.org/School.

    """
    type_: str = Field("School", const=True, alias='@type')
    

School.update_forward_refs()
