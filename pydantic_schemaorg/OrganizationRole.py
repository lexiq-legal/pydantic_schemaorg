from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.Role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    See https://schema.org/OrganizationRole.

    """
    type_: str = Field("OrganizationRole", const=True, alias='@type')
    numberedPosition: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="A number associated with a role in an organization, for example, the number on an athlete's"
     "jersey.",
    )
    

OrganizationRole.update_forward_refs()
