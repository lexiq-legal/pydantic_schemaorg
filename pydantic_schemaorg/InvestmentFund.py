from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InvestmentOrDeposit import InvestmentOrDeposit


class InvestmentFund(InvestmentOrDeposit):
    """A company or fund that gathers capital from a number of investors to create a pool of money"
     "that is then re-invested into stocks, bonds and other assets.

    See: https://schema.org/InvestmentFund
    Model depth: 6
    """

    type_: str = Field("InvestmentFund", const=True, alias="@type")


if TYPE_CHECKING:

    InvestmentFund.update_forward_refs()
