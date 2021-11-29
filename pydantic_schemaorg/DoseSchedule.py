from pydantic import Field
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement.

    See https://schema.org/DoseSchedule.

    """

    targetPopulation: Optional[Union[List[str], str]] = Field(
        None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    doseValue: Union[List[Union[Decimal, Any]], Union[Decimal, Any]] = Field(
        None,
        description="The value of the dose, e.g. 500.",
    )
    doseUnit: Optional[Union[List[str], str]] = Field(
        None,
        description="The unit of the dose, e.g. 'mg'.",
    )
    frequency: Optional[Union[List[str], str]] = Field(
        None,
        description="How often the dose is taken, e.g. 'daily'.",
    )
    locals().update({"@type": Field("DoseSchedule", const=True)})


DoseSchedule.update_forward_refs()
