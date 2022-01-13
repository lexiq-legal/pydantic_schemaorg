from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative"
     "capacity that relies on invasive (surgical), non-invasive, or other techniques.

    See: https://schema.org/MedicalProcedure
    Model depth: 3
    """

    type_: str = Field("MedicalProcedure", const=True, alias="@type")
    procedureType: "Optional[Union[List[Union[MedicalProcedureType, str]], Union[MedicalProcedureType, str]]]" = Field(
        None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",
    )
    howPerformed: "Optional[Union[List[str], str]]" = Field(
        None,
        description="How the procedure is performed.",
    )
    preparation: "Optional[Union[List[Union[str, MedicalEntity]], Union[str, MedicalEntity]]]" = Field(
        None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",
    )
    status: "Optional[Union[List[Union[str, EventStatusType, MedicalStudyStatus]], Union[str, EventStatusType, MedicalStudyStatus]]]" = Field(
        None,
        description="The status of the study (enumerated).",
    )
    bodyLocation: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Location in the body of the anatomical structure.",
    )
    followup: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Typical or recommended followup care after the procedure is performed.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType

    from pydantic_schemaorg.MedicalEntity import MedicalEntity

    from pydantic_schemaorg.EventStatusType import EventStatusType

    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus

    MedicalProcedure.update_forward_refs()
