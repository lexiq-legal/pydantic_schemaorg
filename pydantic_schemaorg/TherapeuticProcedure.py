from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MedicalEntity import MedicalEntity
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving"
     "a health condition.

    See https://schema.org/TherapeuticProcedure.

    """

    doseSchedule: Any = Field(
        None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",
    )
    adverseOutcome: Optional[Union[List[MedicalEntity], MedicalEntity]] = Field(
        None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or is otherwise life-threatening or requires immediate medical"
     "attention), tag it as a seriouseAdverseOutcome instead.",
    )
    drug: Any = Field(
        None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    locals().update({"@type": Field("TherapeuticProcedure", const=True)})


TherapeuticProcedure.update_forward_refs()
