from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.Organization import Organization


class EducationalOrganization(CivicStructure, Organization):
    """An educational organization.

    See: https://schema.org/EducationalOrganization
    Model depth: 3
    """
    type_: str = Field("EducationalOrganization", alias='@type')
    alumni: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Alumni of an organization.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
