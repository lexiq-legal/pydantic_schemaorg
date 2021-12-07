from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Action import Action


class SearchAction(Action):
    """The act of searching for an object. Related actions: * [[FindAction]]: SearchAction"
     "generally leads to a FindAction, but not necessarily.

    See https://schema.org/SearchAction.

    """
    type_: str = Field("SearchAction", const=True, alias='@type')
    query: Optional[Union[List[str], str]] = Field(
        None,
        description="A sub property of instrument. The query used on this action.",
    )
    

SearchAction.update_forward_refs()
