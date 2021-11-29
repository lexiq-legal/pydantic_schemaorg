from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Union, List, Optional
from pydantic_schemaorg.UpdateAction import UpdateAction


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    See https://schema.org/ReplaceAction.

    """

    replacer: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The object that replaces.",
    )
    replacee: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="A sub property of object. The object that is being replaced.",
    )
    locals().update({"@type": Field("ReplaceAction", const=True)})


ReplaceAction.update_forward_refs()
