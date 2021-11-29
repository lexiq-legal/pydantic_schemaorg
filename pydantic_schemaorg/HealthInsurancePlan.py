from pydantic import Field, AnyUrl
from pydantic_schemaorg.ContactPoint import ContactPoint
from typing import Any, Union, List, Optional
from pydantic_schemaorg.HealthPlanNetwork import HealthPlanNetwork
from pydantic_schemaorg.Intangible import Intangible


class HealthInsurancePlan(Intangible):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    See https://schema.org/HealthInsurancePlan.

    """

    contactPoint: Optional[Union[List[ContactPoint], ContactPoint]] = Field(
        None,
        description="A contact point for a person or organization.",
    )
    healthPlanDrugOption: Optional[Union[List[str], str]] = Field(
        None,
        description="TODO.",
    )
    healthPlanMarketingUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="The URL that goes directly to the plan brochure for the specific standard plan or plan"
     "variation.",
    )
    usesHealthPlanIdStandard: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="The standard for interpreting thePlan ID. The preferred is \"HIOS\". See the Centers"
     "for Medicare & Medicaid Services for more details.",
    )
    benefitsSummaryUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="The URL that goes directly to the summary of benefits and coverage for the specific standard"
     "plan or plan variation.",
    )
    healthPlanId: Optional[Union[List[str], str]] = Field(
        None,
        description="The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across"
     "different markets.)",
    )
    includesHealthPlanNetwork: Optional[Union[List[HealthPlanNetwork], HealthPlanNetwork]] = Field(
        None,
        description="Networks covered by this plan.",
    )
    healthPlanDrugTier: Optional[Union[List[str], str]] = Field(
        None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    includesHealthPlanFormulary: Any = Field(
        None,
        description="Formularies covered by this plan.",
    )
    locals().update({"@type": Field("HealthInsurancePlan", const=True)})


HealthInsurancePlan.update_forward_refs()
