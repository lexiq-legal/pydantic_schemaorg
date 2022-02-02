from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See: https://schema.org/SeekToAction
    Model depth: 3
    """
    type_: str = Field("SeekToAction", alias='@type')
    startOffset: Optional[Union[List[Union[Decimal, 'Number', 'HyperTocEntry', str]], Decimal, 'Number', 'HyperTocEntry', str]] = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
