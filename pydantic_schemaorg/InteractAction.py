from pydantic import Field
from pydantic_schemaorg.Action import Action


class InteractAction(Action):
    """The act of interacting with another person or organization.

    See https://schema.org/InteractAction.

    """

    locals().update({"@type": Field("InteractAction", const=True)})


InteractAction.update_forward_refs()
