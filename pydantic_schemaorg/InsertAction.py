from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import List, Optional, Union
from pydantic_schemaorg.AddAction import AddAction


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection.

    See https://schema.org/InsertAction.

    """
    type_: str = Field("InsertAction", const=True, alias='@type')
    toLocation: Optional[Union[List[Union[Place, str]], Union[Place, str]]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    

InsertAction.update_forward_refs()
