from pydantic import Field
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.TradeAction import TradeAction


class DonateAction(TradeAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic"
     "reasons.

    See https://schema.org/DonateAction.

    """
    type_: str = Field("DonateAction", const=True, alias='@type')
    recipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

DonateAction.update_forward_refs()
