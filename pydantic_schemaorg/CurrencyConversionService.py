from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FinancialProduct import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency.

    See: https://schema.org/CurrencyConversionService
    Model depth: 5
    """

    type_: str = Field("CurrencyConversionService", const=True, alias="@type")


if TYPE_CHECKING:

    CurrencyConversionService.update_forward_refs()
