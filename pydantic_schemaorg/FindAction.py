from pydantic import Field
from pydantic_schemaorg.Action import Action


class FindAction(Action):
    """The act of finding an object. Related actions: * [[SearchAction]]: FindAction is generally"
     "lead by a SearchAction, but not necessarily.

    See https://schema.org/FindAction.

    """
    type_: str = Field("FindAction", const=True, alias='@type')
    

FindAction.update_forward_refs()
