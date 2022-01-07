from pydantic import Field
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.AllocateAction import AllocateAction


class AuthorizeAction(AllocateAction):
    """The act of granting permission to an object.

    See https://schema.org/AuthorizeAction.

    """
    type_: str = Field("AuthorizeAction", const=True, alias='@type')
    recipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

AuthorizeAction.update_forward_refs()
