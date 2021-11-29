from pydantic import Field
from pydantic_schema_org.MedicalSpecialty import MedicalSpecialty
from typing import Any, Optional, Union, List
from pydantic_schema_org.MedicalProcedure import MedicalProcedure
from pydantic_schema_org.MedicalTherapy import MedicalTherapy
from pydantic_schema_org.MedicalTest import MedicalTest
from pydantic_schema_org.MedicalBusiness import MedicalBusiness
from pydantic_schema_org.MedicalOrganization import MedicalOrganization


class MedicalClinic(MedicalBusiness, MedicalOrganization):
    """A facility, often associated with a hospital or medical school, that is devoted to the"
     "specific diagnosis and/or healthcare. Previously limited to outpatients but with"
     "evolution it may be open to inpatients as well.

    See https://schema.org/MedicalClinic.

    """

    medicalSpecialty: Optional[Union[List[MedicalSpecialty], MedicalSpecialty]] = Field(
        None,
        description="A medical specialty of the provider.",
    )
    availableService: Optional[Union[List[Union[MedicalProcedure, MedicalTherapy, MedicalTest]], Union[MedicalProcedure, MedicalTherapy, MedicalTest]]] = Field(
        None,
        description="A medical service available from this provider.",
    )
    locals().update({"@type": Field("MedicalClinic", const=True)})


MedicalClinic.update_forward_refs()
