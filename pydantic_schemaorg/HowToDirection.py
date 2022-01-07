from pydantic import AnyUrl, Field
from pydantic_schemaorg.MediaObject import MediaObject
from typing import List, Optional, Union
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.HowToTool import HowToTool
from pydantic_schemaorg.HowToSupply import HowToSupply
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToDirection(ListItem, CreativeWork):
    """A direction indicating a single action to do in the instructions for how to achieve a result.

    See https://schema.org/HowToDirection.

    """
    type_: str = Field("HowToDirection", const=True, alias='@type')
    duringMedia: Optional[Union[List[Union[AnyUrl, MediaObject, str]], Union[AnyUrl, MediaObject, str]]] = Field(
        None,
        description="A media object representing the circumstances while performing this direction.",
    )
    beforeMedia: Optional[Union[List[Union[AnyUrl, MediaObject, str]], Union[AnyUrl, MediaObject, str]]] = Field(
        None,
        description="A media object representing the circumstances before performing this direction.",
    )
    prepTime: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction,"
     "in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    totalTime: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The total time required to perform instructions or a direction (including time to prepare"
     "the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    performTime: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The length of time it takes to perform instructions or a direction (not including time"
     "to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    tool: Optional[Union[List[Union[str, HowToTool]], Union[str, HowToTool]]] = Field(
        None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions"
     "or a direction.",
    )
    afterMedia: Optional[Union[List[Union[AnyUrl, MediaObject, str]], Union[AnyUrl, MediaObject, str]]] = Field(
        None,
        description="A media object representing the circumstances after performing this direction.",
    )
    supply: Optional[Union[List[Union[str, HowToSupply]], Union[str, HowToSupply]]] = Field(
        None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    

HowToDirection.update_forward_refs()
