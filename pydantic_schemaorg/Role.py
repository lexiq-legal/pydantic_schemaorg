from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from datetime import date, datetime
from pydantic_schemaorg.Intangible import Intangible


class Role(Intangible):
    """Represents additional information about a relationship or property. For example a"
     "Role can be used to say that a 'member' role linking some SportsTeam to a player occurred"
     "during a particular time period. Or that a Person's 'actor' role in a Movie was for some"
     "particular characterName. Such properties can be attached to a Role entity, which is"
     "then associated with the main entities using ordinary properties like 'member' or 'actor'."
     "See also [blog post](http://blog.schema.org/2014/06/introducing-role.html).

    See https://schema.org/Role.

    """

    roleName: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A role played, performed or filled by a person or organization. For example, the team"
     "of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer';"
     "or an athlete in a SportsTeam might play in the position named 'Quarterback'.",
    )
    endDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    namedPosition: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A position played, performed or filled by a person or organization, as part of an organization."
     "For example, an athlete in a SportsTeam might play in the position named 'Quarterback'.",
    )
    startDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    locals().update({"@type": Field("Role", const=True)})


Role.update_forward_refs()
