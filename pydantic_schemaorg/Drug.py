from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictBool, AnyUrl
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Substance import Substance


class Drug(Substance):
    """A chemical or biologic substance, used as a medical therapy, that has a physiological"
     "effect on an organism. Here the term drug is used interchangeably with the term medicine"
     "although clinical knowledge make a clear difference between them.

    See: https://schema.org/Drug
    Model depth: 4
    """
    type_: str = Field("Drug", alias='@type')
    prescribingInfo: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="Link to prescribing information for the drug.",
    )
    clinicalPharmacology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Description of the absorption and elimination of drugs, including their concentration"
     "(pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).",
    )
    administrationRoute: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A route by which this drug may be administered, e.g. 'oral'.",
    )
    clincalPharmacology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Description of the absorption and elimination of drugs, including their concentration"
     "(pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).",
    )
    availableStrength: Optional[Union[List[Union['DrugStrength', str]], 'DrugStrength', str]] = Field(
        None,
        description="An available dosage strength for the drug.",
    )
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    pregnancyWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any precaution, guidance, contraindication, etc. related to this drug's use during"
     "pregnancy.",
    )
    breastfeedingWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding"
     "mothers.",
    )
    pregnancyCategory: Optional[Union[List[Union['DrugPregnancyCategory', str]], 'DrugPregnancyCategory', str]] = Field(
        None,
        description="Pregnancy category of this drug.",
    )
    alcoholWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any precaution, guidance, contraindication, etc. related to consumption of alcohol"
     "while taking this drug.",
    )
    drugUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    proprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    manufacturer: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The manufacturer of the product.",
    )
    rxcui: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The RxCUI drug identifier from RXNORM.",
    )
    foodWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any precaution, guidance, contraindication, etc. related to consumption of specific"
     "foods while taking this drug.",
    )
    doseSchedule: Optional[Union[List[Union['DoseSchedule', str]], 'DoseSchedule', str]] = Field(
        None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    isAvailableGenerically: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="True if the drug is available in a generic form (regardless of name).",
    )
    prescriptionStatus: Optional[Union[List[Union[str, 'Text', 'DrugPrescriptionStatus']], str, 'Text', 'DrugPrescriptionStatus']] = Field(
        None,
        description="Indicates the status of drug prescription eg. local catalogs classifications or whether"
     "the drug is available by prescription or over-the-counter, etc.",
    )
    overdosage: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any information related to overdose on a drug, including signs or symptoms, treatments,"
     "contact information for emergency response.",
    )
    includedInHealthInsurancePlan: Optional[Union[List[Union['HealthInsurancePlan', str]], 'HealthInsurancePlan', str]] = Field(
        None,
        description="The insurance plans that cover this drug.",
    )
    nonProprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The generic name of this drug or supplement.",
    )
    dosageForm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension',"
     "'injection'.",
    )
    labelDetails: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="Link to the drug's label details.",
    )
    interactingDrug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        None,
        description="Another drug that is known to interact with this drug in a way that impacts the effect of"
     "this drug or causes a risk to the patient. Note: disease interactions are typically captured"
     "as contraindications.",
    )
    relatedDrug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        None,
        description="Any other drug related to this one, for example commonly-prescribed alternatives.",
    )
    drugClass: Optional[Union[List[Union['DrugClass', str]], 'DrugClass', str]] = Field(
        None,
        description="The class of drug this belongs to (e.g., statins).",
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
    warning: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Any FDA or other warnings about the drug (text or URL).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DrugStrength import DrugStrength
    from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DoseSchedule import DoseSchedule
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus
    from pydantic_schemaorg.HealthInsurancePlan import HealthInsurancePlan
    from pydantic_schemaorg.DrugClass import DrugClass
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
