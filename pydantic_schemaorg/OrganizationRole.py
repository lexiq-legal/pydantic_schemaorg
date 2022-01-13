from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Role import Role


class OrganizationRole(Role):
    """A subclass of Role used to describe roles within organizations.

    See: https://schema.org/OrganizationRole
    Model depth: 4
    """

    type_: str = Field("OrganizationRole", const=True, alias="@type")
    numberedPosition: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="A number associated with a role in an organization, for example, the number on an athlete's"
        "jersey.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    OrganizationRole.update_forward_refs()
