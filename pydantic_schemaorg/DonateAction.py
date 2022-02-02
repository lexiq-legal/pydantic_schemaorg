from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.TradeAction import TradeAction


class DonateAction(TradeAction):
    """The act of providing goods, services, or money without compensation, often for philanthropic"
     "reasons.

    See: https://schema.org/DonateAction
    Model depth: 4
    """
    type_: str = Field("DonateAction", alias='@type')
    recipient: Optional[Union[List[Union['Person', 'Audience', 'Organization', 'ContactPoint', str]], 'Person', 'Audience', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ContactPoint import ContactPoint
