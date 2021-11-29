from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Vessel import Vessel


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart.

    See https://schema.org/Artery.

    """

    supplyTo: Optional[Union[List[AnatomicalStructure], AnatomicalStructure]] = Field(
        None,
        description="The area to which the artery supplies blood.",
    )
    arterialBranch: Optional[Union[List[AnatomicalStructure], AnatomicalStructure]] = Field(
        None,
        description="The branches that comprise the arterial structure.",
    )
    locals().update({"@type": Field("Artery", const=True)})


Artery.update_forward_refs()
