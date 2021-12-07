from pydantic import Field
from pydantic_schemaorg.RadioChannel import RadioChannel


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM.

    See https://schema.org/AMRadioChannel.

    """
    type_: str = Field("AMRadioChannel", const=True, alias='@type')
    

AMRadioChannel.update_forward_refs()
