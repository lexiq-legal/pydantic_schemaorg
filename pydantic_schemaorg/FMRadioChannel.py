from pydantic import Field
from pydantic_schemaorg.RadioChannel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    See https://schema.org/FMRadioChannel.

    """
    type_: str = Field("FMRadioChannel", const=True, alias='@type')
    

FMRadioChannel.update_forward_refs()
