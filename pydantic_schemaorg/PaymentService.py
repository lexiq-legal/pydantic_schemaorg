from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class PaymentService(FinancialProduct):
    """A Service to transfer funds from a person or organization to a beneficiary person or organization.

    See https://schema.org/PaymentService.

    """

    locals().update({"@type": Field("PaymentService", const=True)})


PaymentService.update_forward_refs()
