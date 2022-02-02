from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement.

    See: https://schema.org/DoseSchedule
    Model depth: 4
    """
    type_: str = Field("DoseSchedule", alias='@type')
    targetPopulation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    doseValue: Optional[Union[List[Union[Decimal, 'Number', 'QualitativeValue', str]], Decimal, 'Number', 'QualitativeValue', str]] = Field(
        None,
        description="The value of the dose, e.g. 500.",
    )
    doseUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The unit of the dose, e.g. 'mg'.",
    )
    frequency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="How often the dose is taken, e.g. 'daily'.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
