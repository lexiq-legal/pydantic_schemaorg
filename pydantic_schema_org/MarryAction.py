from pydantic import Field
from pydantic_schema_org.InteractAction import InteractAction


class MarryAction(InteractAction):
    """The act of marrying a person.

    See https://schema.org/MarryAction.

    """

    locals().update({"@type": Field("MarryAction", const=True)})


MarryAction.update_forward_refs()
