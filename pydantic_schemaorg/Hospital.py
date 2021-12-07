from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Dataset import Dataset
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization
from pydantic_schemaorg.EmergencyService import EmergencyService


class Hospital(CivicStructure, MedicalOrganization, EmergencyService):
    """A hospital.

    See https://schema.org/Hospital.

    """
    type_: str = Field("Hospital", const=True, alias='@type')
    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    healthcareReportingData: Union[List[Union[Dataset, Any]], Union[Dataset, Any]] = Field(
        None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
     "[[Dataset]].",
    )
    availableService: Optional[Union[List[Union[MedicalTherapy, MedicalTest, MedicalProcedure]], Union[MedicalTherapy, MedicalTest, MedicalProcedure]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    

Hospital.update_forward_refs()
