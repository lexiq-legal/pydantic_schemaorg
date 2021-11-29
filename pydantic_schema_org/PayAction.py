from pydantic import Field
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TradeAction import TradeAction


class PayAction(TradeAction):
    """An agent pays a price to a participant.

    See https://schema.org/PayAction.

    """

    recipient: Union[List[Union[Audience, Person, Organization, Any]], Union[Audience, Person, Organization, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("PayAction", const=True)})


PayAction.update_forward_refs()
