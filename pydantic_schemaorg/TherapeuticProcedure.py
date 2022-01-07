from pydantic import Field
from pydantic_schemaorg.DoseSchedule import DoseSchedule
from typing import List, Optional, Union
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.Drug import Drug
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving"
     "a health condition.

    See https://schema.org/TherapeuticProcedure.

    """
    type_: str = Field("TherapeuticProcedure", const=True, alias='@type')
    doseSchedule: Optional[Union[List[Union[DoseSchedule, str]], Union[DoseSchedule, str]]] = Field(
        None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",
    )
    adverseOutcome: Optional[Union[List[Union[MedicalEntity, str]], Union[MedicalEntity, str]]] = Field(
        None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or is otherwise life-threatening or requires immediate medical"
     "attention), tag it as a seriouseAdverseOutcome instead.",
    )
    drug: Optional[Union[List[Union[Drug, str]], Union[Drug, str]]] = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    

TherapeuticProcedure.update_forward_refs()
