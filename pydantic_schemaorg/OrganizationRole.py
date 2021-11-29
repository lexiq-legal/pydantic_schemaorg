from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    See https://schema.org/OrganizationRole.

    """

    numberedPosition: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="A number associated with a role in an organization, for example, the number on an athlete's"
     "jersey.",
    )
    locals().update({"@type": Field("OrganizationRole", const=True)})


OrganizationRole.update_forward_refs()
