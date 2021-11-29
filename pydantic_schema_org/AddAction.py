from pydantic import Field
from pydantic_schema_org.UpdateAction import UpdateAction


class AddAction(UpdateAction):
    """The act of editing by adding an object to a collection.

    See https://schema.org/AddAction.

    """

    locals().update({"@type": Field("AddAction", const=True)})


AddAction.update_forward_refs()
