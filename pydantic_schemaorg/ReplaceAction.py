from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    See: https://schema.org/ReplaceAction
    Model depth: 4
    """
    type_: str = Field("ReplaceAction", alias='@type')
    replacer: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A sub property of object. The object that replaces.",
    )
    replacee: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="A sub property of object. The object that is being replaced.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
