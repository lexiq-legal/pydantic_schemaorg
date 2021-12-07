from pydantic import Field
from pydantic_schemaorg.Action import Action


class CreateAction(Action):
    """The act of deliberately creating/producing/generating/building a result out of the"
     "agent.

    See https://schema.org/CreateAction.

    """
    type_: str = Field("CreateAction", const=True, alias='@type')
    

CreateAction.update_forward_refs()
