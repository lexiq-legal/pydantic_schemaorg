from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Intangible import Intangible


class Class(Intangible):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    See https://schema.org/Class.

    """

    supersededBy: Union[List[Union[Enumeration, Any]], Union[Enumeration, Any]] = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    locals().update({"@type": Field("Class", const=True)})


Class.update_forward_refs()
