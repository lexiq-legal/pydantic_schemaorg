from pydantic import AnyUrl, Field
from typing import List, Optional, Union
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FinancialService(LocalBusiness):
    """Financial services business.

    See https://schema.org/FinancialService.

    """
    type_: str = Field("FinancialService", const=True, alias='@type')
    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    

FinancialService.update_forward_refs()
