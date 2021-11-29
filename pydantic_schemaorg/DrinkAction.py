from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids.

    See https://schema.org/DrinkAction.

    """

    locals().update({"@type": Field("DrinkAction", const=True)})


DrinkAction.update_forward_refs()
