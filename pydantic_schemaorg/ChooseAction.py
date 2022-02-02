from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.AssessAction import AssessAction


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    See: https://schema.org/ChooseAction
    Model depth: 4
    """
    type_: str = Field("ChooseAction", alias='@type')
    option: Optional[Union[List[Union[str, 'Text', 'Thing']], str, 'Text', 'Thing']] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    actionOption: Optional[Union[List[Union[str, 'Text', 'Thing']], str, 'Text', 'Thing']] = Field(
        None,
        description="A sub property of object. The options subject to this action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
