from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    See: https://schema.org/OrganizationRole
    Model depth: 4
    """
    type_: str = Field(default="OrganizationRole", alias='@type')
    numberedPosition: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        default=None,
        description="A number associated with a role in an organization, for example, the number on an athlete's"
     "jersey.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
