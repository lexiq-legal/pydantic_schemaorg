from pydantic import Field
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See https://schema.org/TipAction.

    """
    type_: str = Field("TipAction", const=True, alias='@type')
    recipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

TipAction.update_forward_refs()
