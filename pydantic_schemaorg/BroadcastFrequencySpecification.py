from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class BroadcastFrequencySpecification(Intangible):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    See: https://schema.org/BroadcastFrequencySpecification
    Model depth: 3
    """
    type_: str = Field("BroadcastFrequencySpecification", alias='@type')
    broadcastSignalModulation: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        None,
        description="The modulation (e.g. FM, AM, etc) used by a particular broadcast service.",
    )
    broadcastFrequencyValue: Optional[Union[List[Union[Decimal, 'Number', 'QuantitativeValue', str]], Decimal, 'Number', 'QuantitativeValue', str]] = Field(
        None,
        description="The frequency in MHz for a particular broadcast.",
    )
    broadcastSubChannel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The subchannel used for the broadcast.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
