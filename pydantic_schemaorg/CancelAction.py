from pydantic import Field
from pydantic_schemaorg.PlanAction import PlanAction


class CancelAction(PlanAction):
    """The act of asserting that a future event/action is no longer going to happen. Related"
     "actions: * [[ConfirmAction]]: The antonym of CancelAction.

    See https://schema.org/CancelAction.

    """
    type_: str = Field("CancelAction", const=True, alias='@type')
    

CancelAction.update_forward_refs()
