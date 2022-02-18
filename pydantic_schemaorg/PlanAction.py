from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future"
     "date.

    See: https://schema.org/PlanAction
    Model depth: 4
    """
    type_: str = Field(default="PlanAction", alias='@type', const=True)
    scheduledTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The time the object is scheduled to.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
