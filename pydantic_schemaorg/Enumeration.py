from pydantic import Field
from pydantic_schemaorg.Class import Class
from pydantic_schemaorg.Property import Property
from typing import List, Optional, Union
from pydantic_schemaorg.Intangible import Intangible


class Enumeration(Intangible):
    """Lists or enumerations—for example, a list of cuisines or music genres, etc.

    See https://schema.org/Enumeration.

    """
    type_: str = Field("Enumeration", const=True, alias='@type')
    supersededBy: Optional[Union[List[Union[Class, 'Enumeration', Property, str]], Union[Class, 'Enumeration', Property, str]]] = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    

Enumeration.update_forward_refs()
