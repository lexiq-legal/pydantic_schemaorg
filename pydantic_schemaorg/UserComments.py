from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.UserInteraction import UserInteraction


class UserComments(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserComments
    Model depth: 4
    """

    type_: str = Field("UserComments", const=True, alias="@type")
    discusses: "Optional[Union[List[Union[CreativeWork, str]], Union[CreativeWork, str]]]" = Field(
        None,
        description="Specifies the CreativeWork associated with the UserComment.",
    )
    commentText: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The text of the UserComment.",
    )
    replyToUrl: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="The URL at which a reply may be posted to the specified UserComment.",
    )
    commentTime: "Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]]" = Field(
        None,
        description="The time at which the UserComment was made.",
    )
    creator: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
        "CreativeWork.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.CreativeWork import CreativeWork

    from pydantic import AnyUrl

    from datetime import date, datetime

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    UserComments.update_forward_refs()
