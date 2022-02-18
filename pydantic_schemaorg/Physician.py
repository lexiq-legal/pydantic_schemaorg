from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Physician(MedicalBusiness, MedicalOrganization):
    """A doctor's office.

    See: https://schema.org/Physician
    Model depth: 4
    """
    type_: str = Field(default="Physician", alias='@type', constant=True)
    medicalSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )
    hospitalAffiliation: Optional[Union[List[Union['Hospital', str]], 'Hospital', str]] = Field(
        default=None,
        description="A hospital with which the physician or office is affiliated.",
    )
    availableService: Optional[Union[List[Union['MedicalProcedure', 'MedicalTest', 'MedicalTherapy', str]], 'MedicalProcedure', 'MedicalTest', 'MedicalTherapy', str]] = Field(
        default=None,
        description="A medical service available from this provider.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Hospital import Hospital
    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
    from pydantic_schemaorg.MedicalTest import MedicalTest
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
