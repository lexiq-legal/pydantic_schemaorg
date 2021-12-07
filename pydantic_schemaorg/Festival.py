from pydantic import Field
from pydantic_schemaorg.Event import Event


class Festival(Event):
    """Event type: Festival.

    See https://schema.org/Festival.

    """
    type_: str = Field("Festival", const=True, alias='@type')
    

Festival.update_forward_refs()
