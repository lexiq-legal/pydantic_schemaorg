from pydantic import StrictBool, Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Organization import Organization


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic.

    See https://schema.org/MedicalOrganization.

    """
    type_: str = Field("MedicalOrganization", const=True, alias='@type')
    medicalSpecialty: Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    isAcceptingNewPatients: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Whether the provider is accepting new patients.",
    )
    healthPlanNetworkId: Optional[Union[List[str], str]] = Field(
        None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
     "plans).",
    )
    

MedicalOrganization.update_forward_refs()
