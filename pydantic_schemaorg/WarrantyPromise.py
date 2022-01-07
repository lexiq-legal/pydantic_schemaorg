from pydantic import Field
from pydantic_schemaorg.WarrantyScope import WarrantyScope
from typing import List, Optional, Union
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.StructuredValue import StructuredValue


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided"
     "to a customer free of charge in case of a defect or malfunction of a product.

    See https://schema.org/WarrantyPromise.

    """
    type_: str = Field("WarrantyPromise", const=True, alias='@type')
    warrantyScope: Optional[Union[List[Union[WarrantyScope, str]], Union[WarrantyScope, str]]] = Field(
        None,
        description="The scope of the warranty promise.",
    )
    durationOfWarranty: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The duration of the warranty promise. Common unitCode values are ANN for year, MON for"
     "months, or DAY for days.",
    )
    

WarrantyPromise.update_forward_refs()
