from pydantic import Field
from pydantic_schemaorg.RadioChannel import RadioChannel


class AMRadioChannel(RadioChannel):
    """A radio channel that uses AM.

    See https://schema.org/AMRadioChannel.

    """

    locals().update({"@type": Field("AMRadioChannel", const=True)})


AMRadioChannel.update_forward_refs()
