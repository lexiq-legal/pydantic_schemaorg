from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.AllocateAction import AllocateAction


class AuthorizeAction(AllocateAction):
    """The act of granting permission to an object.

    See: https://schema.org/AuthorizeAction
    Model depth: 5
    """

    type_: str = Field("AuthorizeAction", const=True, alias="@type")
    recipient: "Optional[Union[List[Union[Audience, ContactPoint, Person, Organization, str]], Union[Audience, ContactPoint, Person, Organization, str]]]" = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.ContactPoint import ContactPoint

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    AuthorizeAction.update_forward_refs()
