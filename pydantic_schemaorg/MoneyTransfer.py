from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class MoneyTransfer(TransferAction):
    """The act of transferring money from one place to another place. This may occur electronically"
     "or physically.

    See: https://schema.org/MoneyTransfer
    Model depth: 4
    """
    type_: str = Field("MoneyTransfer", alias='@type')
    amount: Optional[Union[List[Union[Decimal, 'Number', 'MonetaryAmount', str]], Decimal, 'Number', 'MonetaryAmount', str]] = Field(
        None,
        description="The amount of money.",
    )
    beneficiaryBank: Optional[Union[List[Union[str, 'Text', 'BankOrCreditUnion']], str, 'Text', 'BankOrCreditUnion']] = Field(
        None,
        description="A bank or bank’s branch, financial institution or international financial institution"
     "operating the beneficiary’s bank account or releasing funds for the beneficiary.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BankOrCreditUnion import BankOrCreditUnion
