from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.StructuredValue import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postalcodes, usually defined as the set of valid codes between [[postalCodeBegin]]"
     "and [[postalCodeEnd]], inclusively.

    See https://schema.org/PostalCodeRangeSpecification.

    """
    type_: str = Field("PostalCodeRangeSpecification", const=True, alias='@type')
    postalCodeEnd: Optional[Union[List[str], str]] = Field(
        None,
        description="Last postal code in the range (included). Needs to be after [[postalCodeBegin]].",
    )
    postalCodeBegin: Optional[Union[List[str], str]] = Field(
        None,
        description="First postal code in a range (included).",
    )
    

PostalCodeRangeSpecification.update_forward_refs()
