from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalStudy import MedicalStudy


class MedicalTrial(MedicalStudy):
    """A medical trial is a type of medical study that uses scientific process used to compare"
     "the safety and efficacy of medical therapies or medical procedures. In general, medical"
     "trials are controlled and subjects are allocated at random to the different treatment"
     "and/or control groups.

    See https://schema.org/MedicalTrial.

    """

    trialDesign: Optional[Union[List[MedicalTrialDesign], MedicalTrialDesign]] = Field(
        None,
        description="Specifics about the trial design (enumerated).",
    )
    locals().update({"@type": Field("MedicalTrial", const=True)})


MedicalTrial.update_forward_refs()
