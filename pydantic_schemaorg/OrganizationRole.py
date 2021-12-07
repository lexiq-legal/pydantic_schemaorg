from pydantic import Field
from decimal import Decimal
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    See https://schema.org/OrganizationRole.

    """
    type_: str = Field("OrganizationRole", const=True, alias='@type')
    numberedPosition: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="A number associated with a role in an organization, for example, the number on an athlete's"
     "jersey.",
    )
    

OrganizationRole.update_forward_refs()
