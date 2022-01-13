from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.TransferAction import TransferAction


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal"
     "of LendAction. Related actions: * [[LendAction]]: Reciprocal of BorrowAction.

    See: https://schema.org/BorrowAction
    Model depth: 4
    """

    type_: str = Field("BorrowAction", const=True, alias="@type")
    lender: "Optional[Union[List[Union[Person, Organization, str]], Union[Person, Organization, str]]]" = Field(
        None,
        description="A sub property of participant. The person that lends the object being borrowed.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Person import Person

    from pydantic_schemaorg.Organization import Organization

    BorrowAction.update_forward_refs()
