from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union, Any
from pydantic_schemaorg.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See https://schema.org/TipAction.

    """

    recipient: Union[List[Union[Organization, Audience, Person, Any]], Union[Organization, Audience, Person, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("TipAction", const=True)})


TipAction.update_forward_refs()
