from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class AccountingService(FinancialService):
    """Accountancy business. As a [[LocalBusiness]] it can be described as a [[provider]]"
     "of one or more [[Service]]\(s).

    See https://schema.org/AccountingService.

    """

    locals().update({"@type": Field("AccountingService", const=True)})


AccountingService.update_forward_refs()
