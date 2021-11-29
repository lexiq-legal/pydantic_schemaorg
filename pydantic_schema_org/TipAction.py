from pydantic import Field
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See https://schema.org/TipAction.

    """

    recipient: Union[List[Union[Audience, Person, Organization, Any]], Union[Audience, Person, Organization, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("TipAction", const=True)})


TipAction.update_forward_refs()
