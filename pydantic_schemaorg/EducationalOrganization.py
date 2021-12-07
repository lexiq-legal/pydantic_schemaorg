from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.Organization import Organization


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization.

    See https://schema.org/EducationalOrganization.

    """
    type_: str = Field("EducationalOrganization", const=True, alias='@type')
    alumni: Optional[Union[List[Person], Person]] = Field(
        None,
        description="Alumni of an organization.",
    )
    

EducationalOrganization.update_forward_refs()
