from pydantic import Field
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.StructuredValue import StructuredValue


class QuantitativeValueDistribution(StructuredValue):
    """A statistical distribution of values.

    See https://schema.org/QuantitativeValueDistribution.

    """

    percentile75: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The 75th percentile value.",
    )
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    percentile25: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The 25th percentile value.",
    )
    percentile90: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The 90th percentile value.",
    )
    percentile10: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The 10th percentile value.",
    )
    median: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The median value.",
    )
    locals().update({"@type": Field("QuantitativeValueDistribution", const=True)})


QuantitativeValueDistribution.update_forward_refs()
