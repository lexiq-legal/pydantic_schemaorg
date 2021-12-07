from pydantic import Field
from pydantic_schemaorg.FindAction import FindAction


class CheckAction(FindAction):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy,"
     "quality, condition, or state.

    See https://schema.org/CheckAction.

    """
    type_: str = Field("CheckAction", const=True, alias='@type')
    

CheckAction.update_forward_refs()
