from pydantic import Field
from pydantic_schemaorg.Action import Action


class CreateAction(Action):
    """The act of deliberately creating/producing/generating/building a result out of the"
     "agent.

    See https://schema.org/CreateAction.

    """

    locals().update({"@type": Field("CreateAction", const=True)})


CreateAction.update_forward_refs()
