from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See: https://schema.org/SeekToAction
    Model depth: 3
    """

    type_: str = Field("SeekToAction", const=True, alias="@type")
    startOffset: "Optional[Union[List[Union[Decimal, HyperTocEntry, str]], Union[Decimal, HyperTocEntry, str]]]" = Field(
        None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
        "work.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry

    SeekToAction.update_forward_refs()
