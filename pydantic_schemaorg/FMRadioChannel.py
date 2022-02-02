from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.RadioChannel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    See: https://schema.org/FMRadioChannel
    Model depth: 5
    """
    type_: str = Field("FMRadioChannel", alias='@type')
    

