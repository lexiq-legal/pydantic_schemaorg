from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided"
     "to a customer free of charge in case of a defect or malfunction of a product.

    See: https://schema.org/WarrantyPromise
    Model depth: 4
    """
    type_: str = Field(default="WarrantyPromise", alias='@type', const=True)
    warrantyScope: Optional[Union[List[Union['WarrantyScope', str]], 'WarrantyScope', str]] = Field(
        default=None,
        description="The scope of the warranty promise.",
    )
    durationOfWarranty: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The duration of the warranty promise. Common unitCode values are ANN for year, MON for"
     "months, or DAY for days.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.WarrantyScope import WarrantyScope
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
