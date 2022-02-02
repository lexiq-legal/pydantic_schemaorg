from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Action import Action


class FindAction(Action):
    """The act of finding an object. Related actions: * [[SearchAction]]: FindAction is generally"
     "lead by a SearchAction, but not necessarily.

    See: https://schema.org/FindAction
    Model depth: 3
    """
    type_: str = Field("FindAction", alias='@type')
    

