from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class BroadcastFrequencySpecification(Intangible):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    See: https://schema.org/BroadcastFrequencySpecification
    Model depth: 3
    """

    type_: str = Field("BroadcastFrequencySpecification", const=True, alias="@type")
    broadcastSignalModulation: "Optional[Union[List[Union[str, QualitativeValue]], Union[str, QualitativeValue]]]" = Field(
        None,
        description="The modulation (e.g. FM, AM, etc) used by a particular broadcast service.",
    )
    broadcastFrequencyValue: "Optional[Union[List[Union[Decimal, QuantitativeValue, str]], Union[Decimal, QuantitativeValue, str]]]" = Field(
        None,
        description="The frequency in MHz for a particular broadcast.",
    )
    broadcastSubChannel: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The subchannel used for the broadcast.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.QualitativeValue import QualitativeValue

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    BroadcastFrequencySpecification.update_forward_refs()
