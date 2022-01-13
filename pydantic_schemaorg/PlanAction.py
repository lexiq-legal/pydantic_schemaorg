from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.OrganizeAction import OrganizeAction


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future"
     "date.

    See: https://schema.org/PlanAction
    Model depth: 4
    """

    type_: str = Field("PlanAction", const=True, alias="@type")
    scheduledTime: "Optional[Union[List[Union[datetime, str]], Union[datetime, str]]]" = Field(
        None,
        description="The time the object is scheduled to.",
    )


if TYPE_CHECKING:

    from datetime import datetime

    PlanAction.update_forward_refs()
