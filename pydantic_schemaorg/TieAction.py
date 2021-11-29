from pydantic import Field
from pydantic_schemaorg.AchieveAction import AchieveAction


class TieAction(AchieveAction):
    """The act of reaching a draw in a competitive activity.

    See https://schema.org/TieAction.

    """

    locals().update({"@type": Field("TieAction", const=True)})


TieAction.update_forward_refs()
