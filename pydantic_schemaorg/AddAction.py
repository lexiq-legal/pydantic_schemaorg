from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    See https://schema.org/AddAction.

    """
    type_: str = Field("AddAction", const=True, alias='@type')
    

AddAction.update_forward_refs()
