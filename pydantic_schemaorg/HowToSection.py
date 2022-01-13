from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.ListItem import ListItem

from pydantic_schemaorg.ItemList import ItemList

from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToSection(ListItem, ItemList, CreativeWork):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for"
     "making a pie crust within a pie recipe).

    See: https://schema.org/HowToSection
    Model depth: 3
    """

    type_: str = Field("HowToSection", const=True, alias="@type")
    steps: "Optional[Union[List[Union[str, ItemList, CreativeWork]], Union[str, ItemList, CreativeWork]]]" = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
        "misnamed 'steps'; 'step' is preferred).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.ItemList import ItemList

    from pydantic_schemaorg.CreativeWork import CreativeWork

    HowToSection.update_forward_refs()
