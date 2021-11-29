from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Role import Role


class PerformanceRole(Role):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance,"
     "e.g. in a Movie, TVSeries etc.

    See https://schema.org/PerformanceRole.

    """

    characterName: Optional[Union[List[str], str]] = Field(
        None,
        description="The name of a character played in some acting or performing role, i.e. in a PerformanceRole.",
    )
    locals().update({"@type": Field("PerformanceRole", const=True)})


PerformanceRole.update_forward_refs()
