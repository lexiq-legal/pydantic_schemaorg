from pydantic import Field
from pydantic_schema_org.FindAction import FindAction


class CheckAction(FindAction):
    """An agent inspects, determines, investigates, inquires, or examines an object's accuracy,"
     "quality, condition, or state.

    See https://schema.org/CheckAction.

    """

    locals().update({"@type": Field("CheckAction", const=True)})


CheckAction.update_forward_refs()
