from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals"
     "use to effect movement.

    See: https://schema.org/Muscle
    Model depth: 4
    """
    type_: str = Field("Muscle", alias='@type')
    nerve: Optional[Union[List[Union['Nerve', str]], 'Nerve', str]] = Field(
        None,
        description="The underlying innervation associated with the muscle.",
    )
    muscleAction: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The movement the muscle generates.",
    )
    antagonist: Optional[Union[List[Union['Muscle', str]], 'Muscle', str]] = Field(
        None,
        description="The muscle whose action counteracts the specified muscle.",
    )
    bloodSupply: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        None,
        description="The blood vessel that carries blood from the heart to the muscle.",
    )
    insertion: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="The place of attachment of a muscle, or what the muscle moves.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Nerve import Nerve
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Vessel import Vessel
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
