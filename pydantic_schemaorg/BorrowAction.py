from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal"
     "of LendAction. Related actions: * [[LendAction]]: Reciprocal of BorrowAction.

    See: https://schema.org/BorrowAction
    Model depth: 4
    """
    type_: str = Field("BorrowAction", alias='@type')
    lender: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="A sub property of participant. The person that lends the object being borrowed.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
