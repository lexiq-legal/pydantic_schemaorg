from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.MedicalStudy import MedicalStudy


class MedicalObservationalStudy(MedicalStudy):
    """An observational study is a type of medical study that attempts to infer the possible"
     "effect of a treatment through observation of a cohort of subjects over a period of time."
     "In an observational study, the assignment of subjects into treatment groups versus"
     "control groups is outside the control of the investigator. This is in contrast with controlled"
     "studies, such as the randomized controlled trials represented by MedicalTrial, where"
     "each subject is randomly assigned to a treatment group or a control group before the start"
     "of the treatment.

    See: https://schema.org/MedicalObservationalStudy
    Model depth: 4
    """
    type_: str = Field("MedicalObservationalStudy", alias='@type')
    studyDesign: Optional[Union[List[Union['MedicalObservationalStudyDesign', str]], 'MedicalObservationalStudyDesign', str]] = Field(
        None,
        description="Specifics about the observational study design (enumerated).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign
