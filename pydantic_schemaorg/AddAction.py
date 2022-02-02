from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    See: https://schema.org/AddAction
    Model depth: 4
    """
    type_: str = Field("AddAction", alias='@type')
    

