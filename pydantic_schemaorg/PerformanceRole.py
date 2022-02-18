from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Role import Role


class PerformanceRole(Role):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance,"
     "e.g. in a Movie, TVSeries etc.

    See: https://schema.org/PerformanceRole
    Model depth: 4
    """
    type_: str = Field(default="PerformanceRole", alias='@type', const=True)
    characterName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of a character played in some acting or performing role, i.e. in a PerformanceRole.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
