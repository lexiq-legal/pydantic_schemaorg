from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class PaymentService(FinancialProduct):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    See: https://schema.org/PaymentService
    Model depth: 5
    """
    type_: str = Field("PaymentService", alias='@type')
    

