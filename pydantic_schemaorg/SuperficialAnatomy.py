from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class SuperficialAnatomy(MedicalEntity):
    """Anatomical features that can be observed by sight (without dissection), including"
     "the form and proportions of the human body as well as surface landmarks that correspond"
     "to deeper subcutaneous structures. Superficial anatomy plays an important role in"
     "sports medicine, phlebotomy, and other medical specialties as underlying anatomical"
     "structures can be identified through surface palpation. For example, during back surgery,"
     "superficial anatomy can be used to palpate and count vertebrae to find the site of incision."
     "Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example,"
     "the median cubital vein can be located by palpating the borders of the cubital fossa (such"
     "as the epicondyles of the humerus) and then looking for the superficial signs of the vein,"
     "such as size, prominence, ability to refill after depression, and feel of surrounding"
     "tissue support. As another example, in a subluxation (dislocation) of the glenohumeral"
     "joint, the bony structure becomes pronounced with the deltoid muscle failing to cover"
     "the glenohumeral joint allowing the edges of the scapula to be superficially visible."
     "Here, the superficial anatomy is the visible edges of the scapula, implying the underlying"
     "dislocation of the joint (the related anatomical structure).

    See https://schema.org/SuperficialAnatomy.

    """

    significance: Optional[Union[List[str], str]] = Field(
        None,
        description="The significance associated with the superficial anatomy; as an example, how characteristics"
     "of the superficial anatomy can suggest underlying medical conditions or courses of"
     "treatment.",
    )
    relatedAnatomy: Union[List[Union[AnatomicalStructure, Any]], Union[AnatomicalStructure, Any]] = Field(
        None,
        description="Anatomical systems or structures that relate to the superficial anatomy.",
    )
    relatedCondition: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="A medical condition associated with this anatomy.",
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
    locals().update({"@type": Field("SuperficialAnatomy", const=True)})


SuperficialAnatomy.update_forward_refs()
