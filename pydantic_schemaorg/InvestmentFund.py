from pydantic import Field
from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money"
     "that is then re-invested into stocks, bonds and other assets.

    See https://schema.org/InvestmentFund.

    """
    type_: str = Field("InvestmentFund", const=True, alias='@type')
    

InvestmentFund.update_forward_refs()
