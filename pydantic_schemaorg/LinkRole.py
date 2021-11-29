from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Language import Language
from pydantic_schemaorg.Role import Role


class LinkRole(Role):
    """A Role that represents a Web link e.g. as expressed via the 'url' property. Its linkRelationship"
     "property can indicate URL-based and plain textual link types e.g. those in IANA link"
     "registry or others such as 'amphtml'. This structure provides a placeholder where details"
     "from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.

    See https://schema.org/LinkRole.

    """

    linkRelationship: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates the relationship type of a Web link.",
    )
    inLanguage: Optional[Union[List[Union[str, Language]], Union[str, Language]]] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    locals().update({"@type": Field("LinkRole", const=True)})


LinkRole.update_forward_refs()
