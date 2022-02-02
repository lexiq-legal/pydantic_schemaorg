from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Joint(AnatomicalStructure):
    """The anatomical location at which two or more bones make contact.

    See: https://schema.org/Joint
    Model depth: 4
    """
    type_: str = Field("Joint", alias='@type')
    functionalClass: Optional[Union[List[Union[str, 'Text', 'MedicalEntity']], str, 'Text', 'MedicalEntity']] = Field(
        None,
        description="The degree of mobility the joint allows.",
    )
    structuralClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The name given to how bone physically connects to each other.",
    )
    biomechnicalClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The biomechanical properties of the bone.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
