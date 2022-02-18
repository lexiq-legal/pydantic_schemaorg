from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.UpdateAction import UpdateAction


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    See: https://schema.org/ReplaceAction
    Model depth: 4
    """
    type_: str = Field(default="ReplaceAction", alias='@type', const=True)
    replacer: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The object that replaces.",
    )
    replacee: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The object that is being replaced.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
