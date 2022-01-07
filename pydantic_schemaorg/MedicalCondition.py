from pydantic import Field
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor
from pydantic_schemaorg.MedicalConditionStage import MedicalConditionStage
from pydantic_schemaorg.DDxElement import DDxElement
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.EventStatusType import EventStatusType
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
from pydantic_schemaorg.Drug import Drug
from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalCondition(MedicalEntity):
    """Any condition of the human body that affects the normal functioning of a person, whether"
     "physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes,"
     "etc.

    See https://schema.org/MedicalCondition.

    """
    type_: str = Field("MedicalCondition", const=True, alias='@type')
    epidemiology: Optional[Union[List[str], str]] = Field(
        None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    typicalTest: Optional[Union[List[Union[MedicalTest, str]], Union[MedicalTest, str]]] = Field(
        None,
        description="A medical test typically performed given this condition.",
    )
    riskFactor: Optional[Union[List[Union[MedicalRiskFactor, str]], Union[MedicalRiskFactor, str]]] = Field(
        None,
        description="A modifiable or non-modifiable factor that increases the risk of a patient contracting"
     "this condition, e.g. age, coexisting condition.",
    )
    stage: Optional[Union[List[Union[MedicalConditionStage, str]], Union[MedicalConditionStage, str]]] = Field(
        None,
        description="The stage of the condition, if applicable.",
    )
    naturalProgression: Optional[Union[List[str], str]] = Field(
        None,
        description="The expected progression of the condition if it is not treated and allowed to progress"
     "naturally.",
    )
    expectedPrognosis: Optional[Union[List[str], str]] = Field(
        None,
        description="The likely outcome in either the short term or long term of the medical condition.",
    )
    differentialDiagnosis: Optional[Union[List[Union[DDxElement, str]], Union[DDxElement, str]]] = Field(
        None,
        description="One of a set of differential diagnoses for the condition. Specifically, a closely-related"
     "or competing diagnosis typically considered later in the cognitive process whereby"
     "this medical condition is distinguished from others most likely responsible for a similar"
     "collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses"
     "in a patient.",
    )
    primaryPrevention: Optional[Union[List[Union[MedicalTherapy, str]], Union[MedicalTherapy, str]]] = Field(
        None,
        description="A preventative therapy used to prevent an initial occurrence of the medical condition,"
     "such as vaccination.",
    )
    possibleTreatment: Optional[Union[List[Union[MedicalTherapy, str]], Union[MedicalTherapy, str]]] = Field(
        None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    status: Optional[Union[List[Union[str, EventStatusType, MedicalStudyStatus]], Union[str, EventStatusType, MedicalStudyStatus]]] = Field(
        None,
        description="The status of the study (enumerated).",
    )
    pathophysiology: Optional[Union[List[str], str]] = Field(
        None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    secondaryPrevention: Optional[Union[List[Union[MedicalTherapy, str]], Union[MedicalTherapy, str]]] = Field(
        None,
        description="A preventative therapy used to prevent reoccurrence of the medical condition after"
     "an initial episode of the condition.",
    )
    drug: Optional[Union[List[Union[Drug, str]], Union[Drug, str]]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    possibleComplication: Optional[Union[List[str], str]] = Field(
        None,
        description="A possible unexpected and unfavorable evolution of a medical condition. Complications"
     "may include worsening of the signs or symptoms of the disease, extension of the condition"
     "to other organ systems, etc.",
    )
    associatedAnatomy: Optional[Union[List[Union[SuperficialAnatomy, AnatomicalStructure, AnatomicalSystem, str]], Union[SuperficialAnatomy, AnatomicalStructure, AnatomicalSystem, str]]] = Field(
        None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    signOrSymptom: Optional[Union[List[Union[MedicalSignOrSymptom, str]], Union[MedicalSignOrSymptom, str]]] = Field(
        None,
        description="A sign or symptom of this condition. Signs are objective or physically observable manifestations"
     "of the medical condition while symptoms are the subjective experience of the medical"
     "condition.",
    )
    

MedicalCondition.update_forward_refs()
