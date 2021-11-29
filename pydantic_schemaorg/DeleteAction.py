from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class DeleteAction(UpdateAction):
    """The act of editing a recipient by removing one of its objects.

    See https://schema.org/DeleteAction.

    """

    locals().update({"@type": Field("DeleteAction", const=True)})


DeleteAction.update_forward_refs()
