from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserComments(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserComments
    Model depth: 4
    """
    type_: str = Field("UserComments", alias='@type')
    discusses: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="Specifies the CreativeWork associated with the UserComment.",
    )
    commentText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The text of the UserComment.",
    )
    replyToUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="The URL at which a reply may be posted to the specified UserComment.",
    )
    commentTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The time at which the UserComment was made.",
    )
    creator: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
