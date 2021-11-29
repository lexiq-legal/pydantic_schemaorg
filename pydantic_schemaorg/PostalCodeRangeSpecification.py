from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.StructuredValue import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postalcodes, usually defined as the set of valid codes between [[postalCodeBegin]]"
     "and [[postalCodeEnd]], inclusively.

    See https://schema.org/PostalCodeRangeSpecification.

    """

    postalCodeEnd: Optional[Union[List[str], str]] = Field(
        None,
        description="Last postal code in the range (included). Needs to be after [[postalCodeBegin]].",
    )
    postalCodeBegin: Optional[Union[List[str], str]] = Field(
        None,
        description="First postal code in a range (included).",
    )
    locals().update({"@type": Field("PostalCodeRangeSpecification", const=True)})


PostalCodeRangeSpecification.update_forward_refs()
