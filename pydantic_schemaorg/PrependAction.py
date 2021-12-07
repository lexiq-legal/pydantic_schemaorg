from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class PrependAction(InsertAction):
    """The act of inserting at the beginning if an ordered collection.

    See https://schema.org/PrependAction.

    """
    type_: str = Field("PrependAction", const=True, alias='@type')
    

PrependAction.update_forward_refs()
