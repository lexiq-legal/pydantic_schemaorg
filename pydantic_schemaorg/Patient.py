from pydantic import Field
from pydantic_schemaorg.MedicalCondition import MedicalCondition
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Drug import Drug
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.MedicalAudience import MedicalAudience


class Patient(Person, MedicalAudience):
    """A patient is any person recipient of health care services.

    See https://schema.org/Patient.

    """
    type_: str = Field("Patient", const=True, alias='@type')
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
    

Patient.update_forward_refs()
