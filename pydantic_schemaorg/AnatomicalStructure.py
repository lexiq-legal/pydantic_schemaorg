from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues,"
     "and cells are all anatomical structures.

    See https://schema.org/AnatomicalStructure.

    """

    diagram: Any = Field(
        None,
        description="An image containing a diagram that illustrates the structure and/or its component substructures"
     "and/or connections with other structures.",
    )
    subStructure: Any = Field(
        None,
        description="Component (sub-)structure(s) that comprise this anatomical structure.",
    )
    connectedTo: Any = Field(
        None,
        description="Other anatomical structures to which this structure is connected.",
    )
    relatedCondition: Any = Field(
        None,
        description="A medical condition associated with this anatomy.",
    )
    bodyLocation: Optional[Union[List[str], str]] = Field(
        None,
        description="Location in the body of the anatomical structure.",
    )
    relatedTherapy: Any = Field(
        None,
        description="A medical therapy related to this anatomy.",
    )
    partOfSystem: Any = Field(
        None,
        description="The anatomical or organ system that this structure is part of.",
    )
    associatedPathophysiology: Optional[Union[List[str], str]] = Field(
        None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    locals().update({"@type": Field("AnatomicalStructure", const=True)})


AnatomicalStructure.update_forward_refs()
