from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.PlayAction import PlayAction


class PerformAction(PlayAction):
    """The act of participating in performance arts.

    See: https://schema.org/PerformAction
    Model depth: 4
    """

    type_: str = Field("PerformAction", const=True, alias="@type")
    entertainmentBusiness: "Optional[Union[List[Union[EntertainmentBusiness, str]], Union[EntertainmentBusiness, str]]]" = Field(
        None,
        description="A sub property of location. The entertainment business where the action occurred.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness

    PerformAction.update_forward_refs()
