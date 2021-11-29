from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.Organization import Organization


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization.

    See https://schema.org/EducationalOrganization.

    """

    alumni: Optional[Union[List[Person], Person]] = Field(
        None,
        description="Alumni of an organization.",
    )
    locals().update({"@type": Field("EducationalOrganization", const=True)})


EducationalOrganization.update_forward_refs()
