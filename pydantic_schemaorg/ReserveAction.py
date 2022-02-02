from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PlanAction import PlanAction


class ReserveAction(PlanAction):
    """Reserving a concrete object. Related actions: * [[ScheduleAction]]: Unlike ScheduleAction,"
     "ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot"
     "/ spatial allocation.

    See: https://schema.org/ReserveAction
    Model depth: 5
    """
    type_: str = Field("ReserveAction", alias='@type')
    

