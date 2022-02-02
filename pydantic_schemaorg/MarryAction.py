from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class MarryAction(InteractAction):
    """The act of marrying a person.

    See: https://schema.org/MarryAction
    Model depth: 4
    """
    type_: str = Field("MarryAction", alias='@type')
    

