from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import Any, Optional, Union, List
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Physician(MedicalBusiness, MedicalOrganization):
    """A doctor's office.

    See https://schema.org/Physician.

    """
    type_: str = Field("Physician", const=True, alias='@type')
    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    hospitalAffiliation: Any = Field(
        None,
        description="A hospital with which the physician or office is affiliated.",
    )
    availableService: Optional[Union[List[Union[MedicalTherapy, MedicalTest, MedicalProcedure]], Union[MedicalTherapy, MedicalTest, MedicalProcedure]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    

Physician.update_forward_refs()
