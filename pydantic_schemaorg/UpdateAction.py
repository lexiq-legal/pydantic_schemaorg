from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    See https://schema.org/UpdateAction.

    """

    collection: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    targetCollection: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    locals().update({"@type": Field("UpdateAction", const=True)})


UpdateAction.update_forward_refs()
