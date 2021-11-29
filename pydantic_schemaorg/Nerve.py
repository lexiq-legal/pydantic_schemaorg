from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along"
     "each of the axons.

    See https://schema.org/Nerve.

    """

    branch: Any = Field(
        None,
        description="The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].",
    )
    nerveMotor: Any = Field(
        None,
        description="The neurological pathway extension that involves muscle control.",
    )
    sensoryUnit: Any = Field(
        None,
        description="The neurological pathway extension that inputs and sends information to the brain or"
     "spinal cord.",
    )
    sourcedFrom: Any = Field(
        None,
        description="The neurological pathway that originates the neurons.",
    )
    locals().update({"@type": Field("Nerve", const=True)})


Nerve.update_forward_refs()
