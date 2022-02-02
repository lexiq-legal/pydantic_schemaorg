from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Action import Action


class ConsumeAction(Action):
    """The act of ingesting information/resources/food.

    See: https://schema.org/ConsumeAction
    Model depth: 3
    """
    type_: str = Field("ConsumeAction", alias='@type')
    actionAccessibilityRequirement: Optional[Union[List[Union['ActionAccessSpecification', str]], 'ActionAccessSpecification', str]] = Field(
        None,
        description="A set of requirements that a must be fulfilled in order to perform an Action. If more than"
     "one value is specied, fulfilling one set of requirements will allow the Action to be performed.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ActionAccessSpecification import ActionAccessSpecification
    from pydantic_schemaorg.Offer import Offer
