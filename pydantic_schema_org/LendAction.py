from pydantic import Field
from pydantic_schema_org.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schema_org.TransferAction import TransferAction


class LendAction(TransferAction):
    """The act of providing an object under an agreement that it will be returned at a later date."
     "Reciprocal of BorrowAction. Related actions: * [[BorrowAction]]: Reciprocal of LendAction.

    See https://schema.org/LendAction.

    """

    borrower: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A sub property of participant. The person that borrows the object being lent.",
    )
    locals().update({"@type": Field("LendAction", const=True)})


LendAction.update_forward_refs()
