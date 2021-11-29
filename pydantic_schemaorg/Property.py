from pydantic import Field
from pydantic_schemaorg.Class import Class
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Enumeration import Enumeration
from pydantic_schemaorg.Intangible import Intangible


class Property(Intangible):
    """A property, used to indicate attributes and relationships of some Thing; equivalent"
     "to rdf:Property.

    See https://schema.org/Property.

    """

    domainIncludes: Optional[Union[List[Class], Class]] = Field(
        None,
        description="Relates a property to a class that is (one of) the type(s) the property is expected to be"
     "used on.",
    )
    rangeIncludes: Optional[Union[List[Class], Class]] = Field(
        None,
        description="Relates a property to a class that constitutes (one of) the expected type(s) for values"
     "of the property.",
    )
    inverseOf: Any = Field(
        None,
        description="Relates a property to a property that is its inverse. Inverse properties relate the same"
     "pairs of items to each other, but in reversed direction. For example, the 'alumni' and"
     "'alumniOf' properties are inverseOf each other. Some properties don't have explicit"
     "inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be"
     "used.",
    )
    supersededBy: Union[List[Union[Enumeration, Class, Any]], Union[Enumeration, Class, Any]] = Field(
        None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    locals().update({"@type": Field("Property", const=True)})


Property.update_forward_refs()
