from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Organization import Organization


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic.

    See: https://schema.org/MedicalOrganization
    Model depth: 3
    """

    type_: str = Field("MedicalOrganization", const=True, alias="@type")
    medicalSpecialty: "Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]]" = Field(
        None,
        description="A medical specialty of the provider.",
    )
    isAcceptingNewPatients: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="Whether the provider is accepting new patients.",
    )
    healthPlanNetworkId: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
        "plans).",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty

    from pydantic import StrictBool

    MedicalOrganization.update_forward_refs()
