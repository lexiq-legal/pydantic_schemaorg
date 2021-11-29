from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class AnatomicalSystem(MedicalEntity):
    """An anatomical system is a group of anatomical structures that work together to perform"
     "a certain task. Anatomical systems, such as organ systems, are one organizing principle"
     "of anatomy, and can includes circulatory, digestive, endocrine, integumentary, immune,"
     "lymphatic, muscular, nervous, reproductive, respiratory, skeletal, urinary, vestibular,"
     "and other systems.

    See https://schema.org/AnatomicalSystem.

    """

    comprisedOf: Union[List[Union[AnatomicalStructure, Any]], Union[AnatomicalStructure, Any]] = Field(
        None,
        description="Specifying something physically contained by something else. Typically used here"
     "for the underlying anatomical structures, such as organs, that comprise the anatomical"
     "system.",
    )
    relatedCondition: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="A medical condition associated with this anatomy.",
    )
    relatedStructure: Optional[Union[List[AnatomicalStructure], AnatomicalStructure]] = Field(
        None,
        description="Related anatomical structure(s) that are not part of the system but relate or connect"
     "to it, such as vascular bundles associated with an organ system.",
    )
    relatedTherapy: Optional[Union[List[MedicalTherapy], MedicalTherapy]] = Field(
        None,
        description="A medical therapy related to this anatomy.",
    )
    associatedPathophysiology: Optional[Union[List[str], str]] = Field(
        None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    locals().update({"@type": Field("AnatomicalSystem", const=True)})


AnatomicalSystem.update_forward_refs()
