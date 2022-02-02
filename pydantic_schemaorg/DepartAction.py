from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MoveAction import MoveAction


class DepartAction(MoveAction):
    """The act of departing from a place. An agent departs from an fromLocation for a destination,"
     "optionally with participants.

    See: https://schema.org/DepartAction
    Model depth: 4
    """
    type_: str = Field("DepartAction", alias='@type')
    

