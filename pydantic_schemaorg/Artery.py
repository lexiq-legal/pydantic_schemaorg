from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Vessel import Vessel


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart.

    See: https://schema.org/Artery
    Model depth: 5
    """
    type_: str = Field("Artery", alias='@type')
    supplyTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="The area to which the artery supplies blood.",
    )
    arterialBranch: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="The branches that comprise the arterial structure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
