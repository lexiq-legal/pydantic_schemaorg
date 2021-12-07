from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Intangible import Intangible


class Enumeration(Intangible):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    See https://schema.org/Enumeration.

    """
    type_: str = Field("Enumeration", const=True, alias='@type')
    supersededBy: Any = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    

Enumeration.update_forward_refs()
