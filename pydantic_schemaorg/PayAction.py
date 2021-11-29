from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union, Any
from pydantic_schemaorg.TradeAction import TradeAction


class PayAction(TradeAction):
    """An agent pays a price to a participant.

    See https://schema.org/PayAction.

    """

    recipient: Union[List[Union[Organization, Audience, Person, Any]], Union[Organization, Audience, Person, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("PayAction", const=True)})


PayAction.update_forward_refs()
