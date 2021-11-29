from pydantic import Field
from datetime import datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future"
     "date.

    See https://schema.org/PlanAction.

    """

    scheduledTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The time the object is scheduled to.",
    )
    locals().update({"@type": Field("PlanAction", const=True)})


PlanAction.update_forward_refs()
