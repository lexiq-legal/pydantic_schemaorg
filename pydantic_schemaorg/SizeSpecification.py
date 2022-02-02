from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.QualitativeValue import QualitativeValue


class SizeSpecification(QualitativeValue):
    """Size related properties of a product, typically a size code ([[name]]) and optionally"
     "a [[sizeSystem]], [[sizeGroup]], and product measurements ([[hasMeasurement]])."
     "In addition, the intended audience can be defined through [[suggestedAge]], [[suggestedGender]],"
     "and suggested body measurements ([[suggestedMeasurement]]).

    See: https://schema.org/SizeSpecification
    Model depth: 5
    """
    type_: str = Field("SizeSpecification", alias='@type')
    sizeSystem: Optional[Union[List[Union[str, 'Text', 'SizeSystemEnumeration']], str, 'Text', 'SizeSystemEnumeration']] = Field(
        None,
        description="The size system used to identify a product's size. Typically either a standard (for example,"
     "\"GS1\" or \"ISO-EN13402\"), country code (for example \"US\" or \"JP\"), or a measuring"
     "system (for example \"Metric\" or \"Imperial\").",
    )
    hasMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    suggestedGender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    sizeGroup: Optional[Union[List[Union[str, 'Text', 'SizeGroupEnumeration']], str, 'Text', 'SizeGroupEnumeration']] = Field(
        None,
        description="The size group (also known as \"size type\") for a product's size. Size groups are common"
     "in the fashion industry to define size segments and suggested audiences for wearable"
     "products. Multiple values can be combined, for example \"men's big and tall\", \"petite"
     "maternity\" or \"regular\"",
    )
    suggestedAge: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    suggestedMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration
