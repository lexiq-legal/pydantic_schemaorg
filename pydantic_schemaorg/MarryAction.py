from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class MarryAction(InteractAction):
    """The act of marrying a person.

    See https://schema.org/MarryAction.

    """
    type_: str = Field("MarryAction", const=True, alias='@type')
    

MarryAction.update_forward_refs()
