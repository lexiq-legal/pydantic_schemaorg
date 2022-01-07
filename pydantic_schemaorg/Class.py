from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.Property import Property
from typing import List, Optional, Union
from pydantic_schemaorg.Intangible import Intangible


class Class(Intangible):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    See https://schema.org/Class.

    """
    type_: str = Field("Class", const=True, alias='@type')
    supersededBy: Optional[Union[List[Union['Class', Enumeration, Property, str]], Union['Class', Enumeration, Property, str]]] = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    

Class.update_forward_refs()
