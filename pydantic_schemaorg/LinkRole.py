from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Role import Role


class LinkRole(Role):
    """A Role that represents a Web link e.g. as expressed via the 'url' property. Its linkRelationship"
     "property can indicate URL-based and plain textual link types e.g. those in IANA link"
     "registry or others such as 'amphtml'. This structure provides a placeholder where details"
     "from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.

    See: https://schema.org/LinkRole
    Model depth: 4
    """
    type_: str = Field("LinkRole", alias='@type')
    linkRelationship: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Indicates the relationship type of a Web link.",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language
