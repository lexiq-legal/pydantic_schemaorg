from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class ReturnAction(TransferAction):
    """The act of returning to the origin that which was previously received (concrete objects)"
     "or taken (ownership).

    See: https://schema.org/ReturnAction
    Model depth: 4
    """
    type_: str = Field(default="ReturnAction", alias='@type', const=True)
    recipient: Optional[Union[List[Union['ContactPoint', 'Audience', 'Organization', 'Person', str]], 'ContactPoint', 'Audience', 'Organization', 'Person', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
