from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.RecommendedDoseSchedule import RecommendedDoseSchedule
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
from pydantic_schemaorg.Substance import Substance


class DietarySupplement(Substance):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the"
     "diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals,"
     "amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.

    See https://schema.org/DietarySupplement.

    """

    safetyConsideration: Optional[Union[List[str], str]] = Field(
        None,
        description="Any potential safety concern associated with the supplement. May include interactions"
     "with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and"
     "documented efficacy of the supplement.",
    )
    recommendedIntake: Optional[Union[List[RecommendedDoseSchedule], RecommendedDoseSchedule]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    targetPopulation: Optional[Union[List[str], str]] = Field(
        None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    activeIngredient: Optional[Union[List[str], str]] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    proprietaryName: Optional[Union[List[str], str]] = Field(
        None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    manufacturer: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The manufacturer of the product.",
    )
    maximumIntake: Any = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    nonProprietaryName: Optional[Union[List[str], str]] = Field(
        None,
        description="The generic name of this drug or supplement.",
    )
    mechanismOfAction: Optional[Union[List[str], str]] = Field(
        None,
        description="The specific biochemical interaction through which this drug or supplement produces"
     "its pharmacological effect.",
    )
    legalStatus: Optional[Union[List[Union[str, DrugLegalStatus, MedicalEnumeration]], Union[str, DrugLegalStatus, MedicalEnumeration]]] = Field(
        None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    isProprietary: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="True if this item's name is a proprietary/brand name (vs. generic name).",
    )
    locals().update({"@type": Field("DietarySupplement", const=True)})


DietarySupplement.update_forward_refs()
