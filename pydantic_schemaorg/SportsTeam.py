from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.SportsOrganization import SportsOrganization


class SportsTeam(SportsOrganization):
    """Organization: Sports team.

    See https://schema.org/SportsTeam.

    """

    gender: Optional[Union[List[Union[str, GenderType]], Union[str, GenderType]]] = Field(
        None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who do not identify as a binary gender."
     "The [[gender]] property can also be used in an extended sense to cover e.g. the gender"
     "of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities."
     "A mixed-gender [[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    athlete: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A person that acts as performing member of a sports team; a player as opposed to a coach.",
    )
    coach: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A person that acts in a coaching role for a sports team.",
    )
    locals().update({"@type": Field("SportsTeam", const=True)})


SportsTeam.update_forward_refs()
