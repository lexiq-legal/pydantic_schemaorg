from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Intangible import Intangible


class Class(Intangible):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    See https://schema.org/Class.

    """
    type_: str = Field("Class", const=True, alias='@type')
    supersededBy: Union[List[Union[Enumeration, Any]], Union[Enumeration, Any]] = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    

Class.update_forward_refs()
