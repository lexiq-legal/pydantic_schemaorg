from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class CurrencyConversionService(FinancialProduct):
    """A service to convert funds from one currency to another currency.

    See https://schema.org/CurrencyConversionService.

    """

    locals().update({"@type": Field("CurrencyConversionService", const=True)})


CurrencyConversionService.update_forward_refs()
