from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class BankOrCreditUnion(FinancialService):
    """Bank or credit union.

    See: https://schema.org/BankOrCreditUnion
    Model depth: 5
    """
    type_: str = Field("BankOrCreditUnion", alias='@type')
    

