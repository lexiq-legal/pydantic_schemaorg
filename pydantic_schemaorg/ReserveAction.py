from pydantic import Field
from pydantic_schemaorg.PlanAction import PlanAction


class ReserveAction(PlanAction):
    """Reserving a concrete object. Related actions: * [[ScheduleAction]]: Unlike ScheduleAction,"
     "ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot"
     "/ spatial allocation.

    See https://schema.org/ReserveAction.

    """

    locals().update({"@type": Field("ReserveAction", const=True)})


ReserveAction.update_forward_refs()
