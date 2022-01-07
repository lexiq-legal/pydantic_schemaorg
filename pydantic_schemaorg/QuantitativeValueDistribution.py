from pydantic import Field
from decimal import Decimal
from typing import List, Optional, Union
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.StructuredValue import StructuredValue


class QuantitativeValueDistribution(StructuredValue):
    """A statistical distribution of values.

    See https://schema.org/QuantitativeValueDistribution.

    """
    type_: str = Field("QuantitativeValueDistribution", const=True, alias='@type')
    percentile75: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The 75th percentile value.",
    )
    duration: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    percentile25: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The 25th percentile value.",
    )
    percentile90: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The 90th percentile value.",
    )
    percentile10: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The 10th percentile value.",
    )
    median: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The median value.",
    )
    

QuantitativeValueDistribution.update_forward_refs()
