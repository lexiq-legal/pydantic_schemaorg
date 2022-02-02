from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues,"
     "and cells are all anatomical structures.

    See: https://schema.org/AnatomicalStructure
    Model depth: 3
    """
    type_: str = Field("AnatomicalStructure", alias='@type')
    diagram: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        None,
        description="An image containing a diagram that illustrates the structure and/or its component substructures"
     "and/or connections with other structures.",
    )
    subStructure: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="Component (sub-)structure(s) that comprise this anatomical structure.",
    )
    connectedTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        None,
        description="Other anatomical structures to which this structure is connected.",
    )
    relatedCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        None,
        description="A medical condition associated with this anatomy.",
    )
    bodyLocation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Location in the body of the anatomical structure.",
    )
    relatedTherapy: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        None,
        description="A medical therapy related to this anatomy.",
    )
    partOfSystem: Optional[Union[List[Union['AnatomicalSystem', str]], 'AnatomicalSystem', str]] = Field(
        None,
        description="The anatomical or organ system that this structure is part of.",
    )
    associatedPathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
