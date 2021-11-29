from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty
from typing import Any, Optional, Union, List
from pydantic_schema_org.Dataset import Dataset
from pydantic_schema_org.MedicalProcedure import MedicalProcedure
from pydantic_schema_org.MedicalTherapy import MedicalTherapy
from pydantic_schema_org.MedicalTest import MedicalTest
from pydantic_schema_org.EmergencyService import EmergencyService
from pydantic_schema_org.MedicalOrganization import MedicalOrganization
from pydantic_schema_org.CivicStructure import CivicStructure


class Hospital(EmergencyService, MedicalOrganization, CivicStructure):
    """A hospital.

    See https://schema.org/Hospital.

    """

    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    healthcareReportingData: Union[List[Union[Dataset, Any]], Union[Dataset, Any]] = Field(
        None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
     "[[Dataset]].",
    )
    availableService: Optional[Union[List[Union[MedicalProcedure, MedicalTherapy, MedicalTest]], Union[MedicalProcedure, MedicalTherapy, MedicalTest]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    locals().update({"@type": Field("Hospital", const=True)})


Hospital.update_forward_refs()
