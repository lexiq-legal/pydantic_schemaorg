from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FinancialService import FinancialService


class AccountingService(FinancialService):
    """Accountancy business. As a [[LocalBusiness]] it can be described as a [[provider]]"
     "of one or more [[Service]]\(s).

    See: https://schema.org/AccountingService
    Model depth: 5
    """

    type_: str = Field("AccountingService", const=True, alias="@type")


if TYPE_CHECKING:

    AccountingService.update_forward_refs()
