from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.BankOrCreditUnion import BankOrCreditUnion
from pydantic_schemaorg.TransferAction import TransferAction


class MoneyTransfer(TransferAction):
    """The act of transferring money from one place to another place. This may occur electronically"
     "or physically.

    See https://schema.org/MoneyTransfer.

    """

    amount: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The amount of money.",
    )
    beneficiaryBank: Optional[Union[List[Union[str, BankOrCreditUnion]], Union[str, BankOrCreditUnion]]] = Field(
        None,
        description="A bank or bank’s branch, financial institution or international financial institution"
     "operating the beneficiary’s bank account or releasing funds for the beneficiary.",
    )
    locals().update({"@type": Field("MoneyTransfer", const=True)})


MoneyTransfer.update_forward_refs()
