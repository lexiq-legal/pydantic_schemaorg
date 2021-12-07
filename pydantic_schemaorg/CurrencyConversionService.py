from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency.

    See https://schema.org/CurrencyConversionService.

    """
    type_: str = Field("CurrencyConversionService", const=True, alias='@type')
    

CurrencyConversionService.update_forward_refs()
