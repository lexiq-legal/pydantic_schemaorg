from pydantic import Field
from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See https://schema.org/SeekToAction.

    """

    startOffset: Optional[Union[List[Union[Decimal, HyperTocEntry]], Union[Decimal, HyperTocEntry]]] = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    locals().update({"@type": Field("SeekToAction", const=True)})


SeekToAction.update_forward_refs()
