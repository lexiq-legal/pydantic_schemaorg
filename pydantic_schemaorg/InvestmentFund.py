from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money"
     "that is then re-invested into stocks, bonds and other assets.

    See: https://schema.org/InvestmentFund
    Model depth: 6
    """
    type_: str = Field("InvestmentFund", alias='@type')
    

