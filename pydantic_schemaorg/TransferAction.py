from pydantic import Field
from pydantic_schemaorg.Place import Place
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Action import Action


class TransferAction(Action):
    """The act of transferring/moving (abstract or concrete) animate or inanimate objects"
     "from one place to another.

    See https://schema.org/TransferAction.

    """

    fromLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    toLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    locals().update({"@type": Field("TransferAction", const=True)})


TransferAction.update_forward_refs()
