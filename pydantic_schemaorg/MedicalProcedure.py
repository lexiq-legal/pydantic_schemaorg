from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
from pydantic_schemaorg.EventStatusType import EventStatusType


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative"
     "capacity that relies on invasive (surgical), non-invasive, or other techniques.

    See https://schema.org/MedicalProcedure.

    """

    procedureType: Any = Field(
        None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",
    )
    howPerformed: Optional[Union[List[str], str]] = Field(
        None,
        description="How the procedure is performed.",
    )
    preparation: Optional[Union[List[Union[str, MedicalEntity]], Union[str, MedicalEntity]]] = Field(
        None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",
    )
    status: Optional[Union[List[Union[str, MedicalStudyStatus, EventStatusType]], Union[str, MedicalStudyStatus, EventStatusType]]] = Field(
        None,
        description="The status of the study (enumerated).",
    )
    bodyLocation: Optional[Union[List[str], str]] = Field(
        None,
        description="Location in the body of the anatomical structure.",
    )
    followup: Optional[Union[List[str], str]] = Field(
        None,
        description="Typical or recommended followup care after the procedure is performed.",
    )
    locals().update({"@type": Field("MedicalProcedure", const=True)})


MedicalProcedure.update_forward_refs()
