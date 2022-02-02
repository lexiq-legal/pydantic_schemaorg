from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative"
     "capacity that relies on invasive (surgical), non-invasive, or other techniques.

    See: https://schema.org/MedicalProcedure
    Model depth: 3
    """
    type_: str = Field("MedicalProcedure", alias='@type')
    procedureType: Optional[Union[List[Union['MedicalProcedureType', str]], 'MedicalProcedureType', str]] = Field(
        None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",
    )
    howPerformed: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="How the procedure is performed.",
    )
    preparation: Optional[Union[List[Union[str, 'Text', 'MedicalEntity']], str, 'Text', 'MedicalEntity']] = Field(
        None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",
    )
    status: Optional[Union[List[Union[str, 'Text', 'MedicalStudyStatus', 'EventStatusType']], str, 'Text', 'MedicalStudyStatus', 'EventStatusType']] = Field(
        None,
        description="The status of the study (enumerated).",
    )
    bodyLocation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Location in the body of the anatomical structure.",
    )
    followup: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Typical or recommended followup care after the procedure is performed.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
    from pydantic_schemaorg.EventStatusType import EventStatusType
