from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection.

    See https://schema.org/AppendAction.

    """
    type_: str = Field("AppendAction", const=True, alias='@type')
    

AppendAction.update_forward_refs()
