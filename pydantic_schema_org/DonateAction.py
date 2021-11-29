from pydantic import Field
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.ContactPoint import ContactPoint
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TradeAction import TradeAction


class DonateAction(TradeAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic"
     "reasons.

    See https://schema.org/DonateAction.

    """

    recipient: Optional[Union[List[Union[Audience, ContactPoint, Person, Organization]], Union[Audience, ContactPoint, Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("DonateAction", const=True)})


DonateAction.update_forward_refs()
