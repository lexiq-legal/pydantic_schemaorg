from pydantic import Field
from pydantic_schema_org.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.CivicStructure import CivicStructure


class EducationalOrganization(Organization, CivicStructure):
    """An educational organization.

    See https://schema.org/EducationalOrganization.

    """

    alumni: Optional[Union[List[Person], Person]] = Field(
        None,
        description="Alumni of an organization.",
    )
    locals().update({"@type": Field("EducationalOrganization", const=True)})


EducationalOrganization.update_forward_refs()
