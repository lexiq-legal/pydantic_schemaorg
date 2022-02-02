from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class QuantitativeValueDistribution(StructuredValue):
    """A statistical distribution of values.

    See: https://schema.org/QuantitativeValueDistribution
    Model depth: 4
    """
    type_: str = Field("QuantitativeValueDistribution", alias='@type')
    percentile75: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The 75th percentile value.",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    percentile25: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The 25th percentile value.",
    )
    percentile90: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The 90th percentile value.",
    )
    percentile10: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The 10th percentile value.",
    )
    median: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The median value.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Duration import Duration
