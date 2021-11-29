from pydantic import Field, AnyUrl
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Union, List, Optional
from datetime import date, datetime
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserComments(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserComments.

    """

    discusses: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Specifies the CreativeWork associated with the UserComment.",
    )
    commentText: Optional[Union[List[str], str]] = Field(
        None,
        description="The text of the UserComment.",
    )
    replyToUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="The URL at which a reply may be posted to the specified UserComment.",
    )
    commentTime: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The time at which the UserComment was made.",
    )
    creator: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    locals().update({"@type": Field("UserComments", const=True)})


UserComments.update_forward_refs()
