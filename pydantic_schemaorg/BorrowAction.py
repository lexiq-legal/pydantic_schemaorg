from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TransferAction import TransferAction


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal"
     "of LendAction. Related actions: * [[LendAction]]: Reciprocal of BorrowAction.

    See https://schema.org/BorrowAction.

    """

    lender: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A sub property of participant. The person that lends the object being borrowed.",
    )
    locals().update({"@type": Field("BorrowAction", const=True)})


BorrowAction.update_forward_refs()
