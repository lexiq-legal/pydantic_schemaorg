from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.StructuredValue import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postalcodes, usually defined as the set of valid codes between [[postalCodeBegin]]"
     "and [[postalCodeEnd]], inclusively.

    See: https://schema.org/PostalCodeRangeSpecification
    Model depth: 4
    """

    type_: str = Field("PostalCodeRangeSpecification", const=True, alias="@type")
    postalCodeEnd: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Last postal code in the range (included). Needs to be after [[postalCodeBegin]].",
    )
    postalCodeBegin: "Optional[Union[List[str], str]]" = Field(
        None,
        description="First postal code in a range (included).",
    )


if TYPE_CHECKING:

    PostalCodeRangeSpecification.update_forward_refs()
