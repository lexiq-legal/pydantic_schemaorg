from pydantic import Field
from pydantic_schema_org.Place import Place
from typing import Any, Optional, Union, List
from pydantic_schema_org.AddAction import AddAction


class InsertAction(AddAction):
    """The act of adding at a specific location in an ordered collection.

    See https://schema.org/InsertAction.

    """

    toLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    locals().update({"@type": Field("InsertAction", const=True)})


InsertAction.update_forward_refs()
