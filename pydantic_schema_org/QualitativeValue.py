from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.PropertyValue import PropertyValue
from pydantic_schema_org.Enumeration import Enumeration
from pydantic_schema_org.MeasurementTypeEnumeration import MeasurementTypeEnumeration
from pydantic_schema_org.DefinedTerm import DefinedTerm
from pydantic_schema_org.StructuredValue import StructuredValue


class QualitativeValue(Enumeration):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or"
     "the garment sizes 'S', 'M', 'L', and 'XL'.

    See https://schema.org/QualitativeValue.

    """

    lesser: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than the object.",
    )
    nonEqual: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is not equal"
     "to the object.",
    )
    equal: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is equal to"
     "the object.",
    )
    lesserOrEqual: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than or equal to the object.",
    )
    greaterOrEqual: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than or equal to the object.",
    )
    greater: Any = Field(
        None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than the object.",
    )
    additionalProperty: Optional[Union[List[PropertyValue], PropertyValue]] = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    valueReference: Union[List[Union[str, Enumeration, PropertyValue, MeasurementTypeEnumeration, DefinedTerm, StructuredValue, Any]], Union[str, Enumeration, PropertyValue, MeasurementTypeEnumeration, DefinedTerm, StructuredValue, Any]] = Field(
        None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    locals().update({"@type": Field("QualitativeValue", const=True)})


QualitativeValue.update_forward_refs()
