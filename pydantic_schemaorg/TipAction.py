from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.TradeAction import TradeAction


class TipAction(TradeAction):
    """The act of giving money voluntarily to a beneficiary in recognition of services rendered.

    See: https://schema.org/TipAction
    Model depth: 4
    """

    type_: str = Field("TipAction", const=True, alias="@type")
    recipient: "Optional[Union[List[Union[Audience, ContactPoint, Person, Organization, str]], Union[Audience, ContactPoint, Person, Organization, str]]]" = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Audience import Audience

    from pydantic_schemaorg.ContactPoint import ContactPoint

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    TipAction.update_forward_refs()
