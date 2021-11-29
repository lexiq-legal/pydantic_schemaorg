from pydantic import Field, AnyUrl
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Service import Service


class FinancialProduct(Service):
    """A product provided to consumers and businesses by financial institutions such as banks,"
     "insurance companies, brokerage firms, consumer finance companies, and investment"
     "companies which comprise the financial services industry.

    See https://schema.org/FinancialProduct.

    """

    annualPercentageRate: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The annual rate that is charged for borrowing (or made by investing), expressed as a single"
     "percentage number that represents the actual yearly cost of funds over the term of a loan."
     "This includes any fees or additional costs associated with the transaction.",
    )
    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    interestRate: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The interest rate, charged or paid, applicable to the financial product. Note: This"
     "is different from the calculated annualPercentageRate.",
    )
    locals().update({"@type": Field("FinancialProduct", const=True)})


FinancialProduct.update_forward_refs()
