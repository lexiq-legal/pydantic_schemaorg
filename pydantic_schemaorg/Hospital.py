from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import List, Optional, Union
from pydantic_schemaorg.CDCPMDRecord import CDCPMDRecord
from pydantic_schemaorg.Dataset import Dataset
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    """A hospital.

    See https://schema.org/Hospital.

    """
    type_: str = Field("Hospital", const=True, alias='@type')
    medicalSpecialty: Optional[Union[List[Union[MedicalSpecialty, str]], Union[MedicalSpecialty, str]]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    healthcareReportingData: Optional[Union[List[Union[CDCPMDRecord, Dataset, str]], Union[CDCPMDRecord, Dataset, str]]] = Field(
        None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
     "[[Dataset]].",
    )
    availableService: Optional[Union[List[Union[MedicalTest, MedicalProcedure, MedicalTherapy, str]], Union[MedicalTest, MedicalProcedure, MedicalTherapy, str]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    

Hospital.update_forward_refs()
