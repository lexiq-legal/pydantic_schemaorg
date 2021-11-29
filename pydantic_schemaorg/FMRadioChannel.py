from pydantic import Field
from pydantic_schemaorg.RadioChannel import RadioChannel


class FMRadioChannel(RadioChannel):
    """A radio channel that uses FM.

    See https://schema.org/FMRadioChannel.

    """

    locals().update({"@type": Field("FMRadioChannel", const=True)})


FMRadioChannel.update_forward_refs()
