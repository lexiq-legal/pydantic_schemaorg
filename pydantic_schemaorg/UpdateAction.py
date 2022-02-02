from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Action import Action


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    See: https://schema.org/UpdateAction
    Model depth: 3
    """
    type_: str = Field("UpdateAction", alias='@type')
    collection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    targetCollection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A sub property of object. The collection target of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
