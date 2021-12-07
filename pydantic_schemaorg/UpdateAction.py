from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Action import Action


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    See https://schema.org/UpdateAction.

    """
    type_: str = Field("UpdateAction", const=True, alias='@type')
    collection: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    targetCollection: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    

UpdateAction.update_forward_refs()
