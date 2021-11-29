from pydantic import Field
from pydantic_schemaorg.Thing import Thing
from typing import Any, Union, List, Optional
from pydantic_schemaorg.AssessAction import AssessAction


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    See https://schema.org/ChooseAction.

    """

    option: Optional[Union[List[Union[str, Thing]], Union[str, Thing]]] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    actionOption: Optional[Union[List[Union[str, Thing]], Union[str, Thing]]] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    locals().update({"@type": Field("ChooseAction", const=True)})


ChooseAction.update_forward_refs()
