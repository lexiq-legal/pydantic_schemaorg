from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement.

    See: https://schema.org/DoseSchedule
    Model depth: 4
    """

    type_: str = Field("DoseSchedule", const=True, alias="@type")
    targetPopulation: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Characteristics of the population for which this is intended, or which typically uses"
        "it, e.g. 'adults'.",
    )
    doseValue: "Optional[Union[List[Union[Decimal, QualitativeValue, str]], Union[Decimal, QualitativeValue, str]]]" = Field(
        None,
        description="The value of the dose, e.g. 500.",
    )
    doseUnit: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The unit of the dose, e.g. 'mg'.",
    )
    frequency: "Optional[Union[List[str], str]]" = Field(
        None,
        description="How often the dose is taken, e.g. 'daily'.",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.QualitativeValue import QualitativeValue

    DoseSchedule.update_forward_refs()
