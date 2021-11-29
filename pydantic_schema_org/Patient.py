from pydantic import Field
from pydantic_schema_org.MedicalCondition import MedicalCondition
from typing import Any, Optional, Union, List
from pydantic_schema_org.Drug import Drug
from pydantic_schema_org.MedicalAudience import MedicalAudience
from pydantic_schema_org.Person import Person


class Patient(MedicalAudience, Person):
    """A patient is any person recipient of health care services.

    See https://schema.org/Patient.

    """

    diagnosis: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="One or more alternative conditions considered in the differential diagnosis process"
     "as output of a diagnosis process.",
    )
    healthCondition: Optional[Union[List[MedicalCondition], MedicalCondition]] = Field(
        None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    drug: Optional[Union[List[Drug], Drug]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    locals().update({"@type": Field("Patient", const=True)})


Patient.update_forward_refs()
