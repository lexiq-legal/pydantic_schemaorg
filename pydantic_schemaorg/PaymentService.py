from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class PaymentService(FinancialProduct):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    See https://schema.org/PaymentService.

    """
    type_: str = Field("PaymentService", const=True, alias='@type')
    

PaymentService.update_forward_refs()
