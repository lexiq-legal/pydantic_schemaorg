from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    See: https://schema.org/InsuranceAgency
    Model depth: 5
    """
    type_: str = Field("InsuranceAgency", alias='@type')
    

