from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Dataset import Dataset
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
from pydantic_schemaorg.MedicalTest import MedicalTest
from pydantic_schemaorg.CivicStructure import CivicStructure
from pydantic_schemaorg.EmergencyService import EmergencyService
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
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
