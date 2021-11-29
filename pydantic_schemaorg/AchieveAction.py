from pydantic import Field
from pydantic_schemaorg.Action import Action


class AchieveAction(Action):
    """The act of accomplishing something via previous efforts. It is an instantaneous action"
     "rather than an ongoing process.

    See https://schema.org/AchieveAction.

    """

    locals().update({"@type": Field("AchieveAction", const=True)})


AchieveAction.update_forward_refs()
