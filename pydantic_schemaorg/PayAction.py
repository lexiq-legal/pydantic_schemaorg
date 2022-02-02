from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class PayAction(TradeAction):
    """An agent pays a price to a participant.

    See: https://schema.org/PayAction
    Model depth: 4
    """
    type_: str = Field("PayAction", alias='@type')
    recipient: Optional[Union[List[Union['Person', 'Audience', 'Organization', 'ContactPoint', str]], 'Person', 'Audience', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ContactPoint import ContactPoint
