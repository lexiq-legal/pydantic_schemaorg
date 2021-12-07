from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Action import Action


class ConsumeAction(Action):
    """The act of ingesting information/resources/food.

    See https://schema.org/ConsumeAction.

    """
    type_: str = Field("ConsumeAction", const=True, alias='@type')
    actionAccessibilityRequirement: Any = Field(
        None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than"
     "one value is specied, fulfilling one set of requirements will allow the Action to be performed.",
    )
    expectsAcceptanceOf: Any = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    

ConsumeAction.update_forward_refs()
