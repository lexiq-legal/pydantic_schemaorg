from pydantic import Field
from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money"
     "that is then re-invested into stocks, bonds and other assets.

    See https://schema.org/InvestmentFund.

    """

    locals().update({"@type": Field("InvestmentFund", const=True)})


InvestmentFund.update_forward_refs()
