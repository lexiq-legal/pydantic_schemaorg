from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See: https://schema.org/SeekToAction
    Model depth: 3
    """
    type_: str = Field(default="SeekToAction", alias='@type', const=True)
    startOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
