from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlanAction import PlanAction


class ScheduleAction(PlanAction):
    """Scheduling future actions, events, or tasks. Related actions: * [[ReserveAction]]:"
     "Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task,"
     "etc) towards a time slot / spatial allocation.

    See: https://schema.org/ScheduleAction
    Model depth: 5
    """
    type_: str = Field("ScheduleAction", alias='@type')
    

