from pydantic import Field
from pydantic_schemaorg.FindAction import FindAction


class DiscoverAction(FindAction):
    """The act of discovering/finding an object.

    See https://schema.org/DiscoverAction.

    """
    type_: str = Field("DiscoverAction", const=True, alias='@type')
    

DiscoverAction.update_forward_refs()
