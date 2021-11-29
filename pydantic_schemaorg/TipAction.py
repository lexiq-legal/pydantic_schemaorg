from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Audience import Audience
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See https://schema.org/TipAction.

    """

    recipient: Union[List[Union[Organization, Person, Audience, Any]], Union[Organization, Person, Audience, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("TipAction", const=True)})


TipAction.update_forward_refs()
