from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class AutomatedTeller(FinancialService):
    """ATM/cash machine.

    See: https://schema.org/AutomatedTeller
    Model depth: 5
    """
    type_: str = Field("AutomatedTeller", alias='@type')
    

