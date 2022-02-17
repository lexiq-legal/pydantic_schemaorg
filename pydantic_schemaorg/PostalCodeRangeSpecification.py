from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class PostalCodeRangeSpecification(StructuredValue):
    """Indicates a range of postalcodes, usually defined as the set of valid codes between [[postalCodeBegin]]"
     "and [[postalCodeEnd]], inclusively.

    See: https://schema.org/PostalCodeRangeSpecification
    Model depth: 4
    """
    type_: str = Field("PostalCodeRangeSpecification", alias='@type')
    postalCodeEnd: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Last postal code in the range (included). Needs to be after [[postalCodeBegin]].",
    )
    postalCodeBegin: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="First postal code in a range (included).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
