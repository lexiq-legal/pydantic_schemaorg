from pydantic import Field
from datetime import datetime
from typing import Any, Optional, Union, List
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future"
     "date.

    See https://schema.org/PlanAction.

    """
    type_: str = Field("PlanAction", const=True, alias='@type')
    scheduledTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The time the object is scheduled to.",
    )
    

PlanAction.update_forward_refs()
