from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class MedicalOrganization(Organization):
    """A medical organization (physical or not), such as hospital, institution or clinic.

    See: https://schema.org/MedicalOrganization
    Model depth: 3
    """
    type_: str = Field("MedicalOrganization", alias='@type')
    medicalSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    isAcceptingNewPatients: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Whether the provider is accepting new patients.",
    )
    healthPlanNetworkId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
     "plans).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
