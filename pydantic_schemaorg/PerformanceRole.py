from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Role import Role


class PerformanceRole(Role):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance,"
     "e.g. in a Movie, TVSeries etc.

    See: https://schema.org/PerformanceRole
    Model depth: 4
    """

    type_: str = Field("PerformanceRole", const=True, alias="@type")
    characterName: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The name of a character played in some acting or performing role, i.e. in a PerformanceRole.",
    )


if TYPE_CHECKING:

    PerformanceRole.update_forward_refs()
