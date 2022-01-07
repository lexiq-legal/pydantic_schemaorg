from pydantic import Field
from decimal import Decimal
from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
from typing import List, Optional, Union
from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See https://schema.org/SeekToAction.

    """
    type_: str = Field("SeekToAction", const=True, alias='@type')
    startOffset: Optional[Union[List[Union[Decimal, HyperTocEntry, str]], Union[Decimal, HyperTocEntry, str]]] = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    

SeekToAction.update_forward_refs()
