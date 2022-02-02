from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Service import Service


class FinancialProduct(Service):
    """A product provided to consumers and businesses by financial institutions such as banks,"
     "insurance companies, brokerage firms, consumer finance companies, and investment"
     "companies which comprise the financial services industry.

    See: https://schema.org/FinancialProduct
    Model depth: 4
    """
    type_: str = Field("FinancialProduct", alias='@type')
    annualPercentageRate: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The annual rate that is charged for borrowing (or made by investing), expressed as a single"
     "percentage number that represents the actual yearly cost of funds over the term of a loan."
     "This includes any fees or additional costs associated with the transaction.",
    )
    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    interestRate: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The interest rate, charged or paid, applicable to the financial product. Note: This"
     "is different from the calculated annualPercentageRate.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
