from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FinancialService import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    See: https://schema.org/AutomatedTeller
    Model depth: 5
    """

    type_: str = Field("AutomatedTeller", const=True, alias="@type")


if TYPE_CHECKING:

    AutomatedTeller.update_forward_refs()
