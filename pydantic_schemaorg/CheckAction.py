from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.FindAction import FindAction


class CheckAction(FindAction):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy,"
     "quality, condition, or state.

    See: https://schema.org/CheckAction
    Model depth: 4
    """
    type_: str = Field("CheckAction", alias='@type')
    

