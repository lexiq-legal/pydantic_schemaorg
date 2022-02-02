from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class PlanAction(OrganizeAction):
    """The act of planning the execution of an event/task/action/reservation/plan to a future"
     "date.

    See: https://schema.org/PlanAction
    Model depth: 4
    """
    type_: str = Field("PlanAction", alias='@type')
    scheduledTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The time the object is scheduled to.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
