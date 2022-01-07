from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import List, Optional, Union
from pydantic_schemaorg.Hospital import Hospital
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Physician(MedicalBusiness, MedicalOrganization):
    """A doctor's office.

    See https://schema.org/Physician.

    """
    type_: str = Field("Physician", const=True, alias='@type')
    medicalSpecialty: Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    hospitalAffiliation: Optional[Union[List[Union[Hospital, str]], Union[Hospital, str]]] = Field(
        None,
        description="A hospital with which the physician or office is affiliated.",
    )
    availableService: Optional[Union[List[Union[MedicalTest, MedicalProcedure, MedicalTherapy, str]], Union[MedicalTest, MedicalProcedure, MedicalTherapy, str]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    

Physician.update_forward_refs()
