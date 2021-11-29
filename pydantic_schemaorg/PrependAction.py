from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class PrependAction(InsertAction):
    """The act of inserting at the beginning if an ordered collection.

    See https://schema.org/PrependAction.

    """

    locals().update({"@type": Field("PrependAction", const=True)})


PrependAction.update_forward_refs()
