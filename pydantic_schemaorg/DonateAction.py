from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union, Any
from pydantic_schemaorg.TradeAction import TradeAction


class DonateAction(TradeAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic"
     "reasons.

    See https://schema.org/DonateAction.

    """

    recipient: Optional[Union[List[Union[Organization, Audience, ContactPoint, Person]], Union[Organization, Audience, ContactPoint, Person]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("DonateAction", const=True)})


DonateAction.update_forward_refs()
