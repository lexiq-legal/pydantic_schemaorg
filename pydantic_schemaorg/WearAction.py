from pydantic import Field
from pydantic_schemaorg.UseAction import UseAction


class WearAction(UseAction):
    """The act of dressing oneself in clothing.

    See https://schema.org/WearAction.

    """

    locals().update({"@type": Field("WearAction", const=True)})


WearAction.update_forward_refs()
