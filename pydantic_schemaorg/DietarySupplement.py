from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.Substance import Substance


class DietarySupplement(Substance):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the"
     "diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals,"
     "amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.

    See: https://schema.org/DietarySupplement
    Model depth: 4
    """
    type_: str = Field("DietarySupplement", alias='@type')
    safetyConsideration: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any potential safety concern associated with the supplement. May include interactions"
     "with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and"
     "documented efficacy of the supplement.",
    )
    recommendedIntake: Optional[Union[List[Union['RecommendedDoseSchedule', str]], 'RecommendedDoseSchedule', str]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    targetPopulation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    proprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    manufacturer: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The manufacturer of the product.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    nonProprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The generic name of this drug or supplement.",
    )
    mechanismOfAction: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The specific biochemical interaction through which this drug or supplement produces"
     "its pharmacological effect.",
    )
    legalStatus: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']], str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']] = Field(
        None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    isProprietary: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="True if this item's name is a proprietary/brand name (vs. generic name).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.RecommendedDoseSchedule import RecommendedDoseSchedule
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.Boolean import Boolean
