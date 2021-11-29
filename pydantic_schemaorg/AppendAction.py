from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection.

    See https://schema.org/AppendAction.

    """

    locals().update({"@type": Field("AppendAction", const=True)})


AppendAction.update_forward_refs()
