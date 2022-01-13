from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FinancialService(LocalBusiness):
    """Financial services business.

    See: https://schema.org/FinancialService
    Model depth: 4
    """

    type_: str = Field("FinancialService", const=True, alias="@type")
    feesAndCommissionsSpecification: "Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]]" = Field(
        None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
        "product, or by a financial service organization.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    FinancialService.update_forward_refs()
