from pydantic import Field
from pydantic_schemaorg.Nerve import Nerve
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Vessel import Vessel
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals"
     "use to effect movement.

    See https://schema.org/Muscle.

    """

    nerve: Optional[Union[List[Nerve], Nerve]] = Field(
        None,
        description="The underlying innervation associated with the muscle.",
    )
    muscleAction: Optional[Union[List[str], str]] = Field(
        None,
        description="The movement the muscle generates.",
    )
    antagonist: Any = Field(
        None,
        description="The muscle whose action counteracts the specified muscle.",
    )
    bloodSupply: Optional[Union[List[Vessel], Vessel]] = Field(
        None,
        description="The blood vessel that carries blood from the heart to the muscle.",
    )
    insertion: Optional[Union[List[AnatomicalStructure], AnatomicalStructure]] = Field(
        None,
        description="The place of attachment of a muscle, or what the muscle moves.",
    )
    locals().update({"@type": Field("Muscle", const=True)})


Muscle.update_forward_refs()
