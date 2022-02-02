from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class CookAction(CreateAction):
    """The act of producing/preparing food.

    See: https://schema.org/CookAction
    Model depth: 4
    """
    type_: str = Field("CookAction", alias='@type')
    recipe: Optional[Union[List[Union['Recipe', str]], 'Recipe', str]] = Field(
        None,
        description="A sub property of instrument. The recipe/instructions used to perform the action.",
    )
    foodEstablishment: Optional[Union[List[Union['Place', 'FoodEstablishment', str]], 'Place', 'FoodEstablishment', str]] = Field(
        None,
        description="A sub property of location. The specific food establishment where the action occurred.",
    )
    foodEvent: Optional[Union[List[Union['FoodEvent', str]], 'FoodEvent', str]] = Field(
        None,
        description="A sub property of location. The specific food event where the action occurred.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Recipe import Recipe
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.FoodEstablishment import FoodEstablishment
    from pydantic_schemaorg.FoodEvent import FoodEvent
