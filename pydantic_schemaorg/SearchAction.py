from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Action import Action


class SearchAction(Action):
    """The act of searching for an object. Related actions: * [[FindAction]]: SearchAction"
     "generally leads to a FindAction, but not necessarily.

    See: https://schema.org/SearchAction
    Model depth: 3
    """
    type_: str = Field(default="SearchAction", alias='@type', const=True)
    query: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A sub property of instrument. The query used on this action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
