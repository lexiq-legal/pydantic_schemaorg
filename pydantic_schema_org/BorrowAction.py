from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TransferAction import TransferAction


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal"
     "of LendAction. Related actions: * [[LendAction]]: Reciprocal of BorrowAction.

    See https://schema.org/BorrowAction.

    """

    lender: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The person that lends the object being borrowed.",
    )
    locals().update({"@type": Field("BorrowAction", const=True)})


BorrowAction.update_forward_refs()
