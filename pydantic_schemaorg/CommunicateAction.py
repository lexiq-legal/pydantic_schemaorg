from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.InteractAction import InteractAction


class CommunicateAction(InteractAction):
    """The act of conveying information to another person via a communication medium (instrument)"
     "such as speech, email, or telephone conversation.

    See: https://schema.org/CommunicateAction
    Model depth: 4
    """

    type_: str = Field("CommunicateAction", const=True, alias="@type")
    about: "Optional[Union[List[Union[Thing, str]], Union[Thing, str]]]" = Field(
        None,
        description="The subject matter of the content.",
    )
    language: "Optional[Union[List[Union[Language, str]], Union[Language, str]]]" = Field(
        None,
        description="A sub property of instrument. The language used on this action.",
    )
    recipient: "Optional[Union[List[Union[Audience, ContactPoint, Person, Organization, str]], Union[Audience, ContactPoint, Person, Organization, str]]]" = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    inLanguage: "Optional[Union[List[Union[str, Language]], Union[str, Language]]]" = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
        "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
        "[[availableLanguage]].",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Thing import Thing

    from pydantic_schemaorg.Language import Language

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.ContactPoint import ContactPoint

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    CommunicateAction.update_forward_refs()
