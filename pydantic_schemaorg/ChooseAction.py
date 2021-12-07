from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Optional, Union, List
from pydantic_schemaorg.AssessAction import AssessAction


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    See https://schema.org/ChooseAction.

    """
    type_: str = Field("ChooseAction", const=True, alias='@type')
    option: Optional[Union[List[Union[str, Thing]], Union[str, Thing]]] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    actionOption: Optional[Union[List[Union[str, Thing]], Union[str, Thing]]] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    

ChooseAction.update_forward_refs()
