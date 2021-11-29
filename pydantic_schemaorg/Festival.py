from pydantic import Field
from pydantic_schemaorg.Event import Event


class Festival(Event):
    """Event type: Festival.

    See https://schema.org/Festival.

    """

    locals().update({"@type": Field("Festival", const=True)})


Festival.update_forward_refs()
