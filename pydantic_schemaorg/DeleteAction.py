from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects.

    See: https://schema.org/DeleteAction
    Model depth: 4
    """
    type_: str = Field("DeleteAction", alias='@type')
    

