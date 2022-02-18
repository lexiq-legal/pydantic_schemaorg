from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit
from pydantic_schemaorg.BankAccount import BankAccount


class DepositAccount(InvestmentOrDeposit, BankAccount):
    """A type of Bank Account with a main purpose of depositing funds to gain interest or other"
     "benefits.

    See: https://schema.org/DepositAccount
    Model depth: 6
    """
    type_: str = Field(default="DepositAccount", alias='@type', const=True)
    
