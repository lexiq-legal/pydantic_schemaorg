from __future__ import annotations
from typing import TYPE_CHECKING

from decimal import Decimal
from typing import Union, Optional, List
from pydantic import AnyUrl, StrictBool


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class QuantitativeValue(StructuredValue):
    """A point value or interval for product characteristics and other purposes.

    See: https://schema.org/QuantitativeValue
    Model depth: 4
    """
    type_: str = Field("QuantitativeValue", alias='@type')
    minValue: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The lower value of some characteristic or property.",
    )
    unitText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    value: Optional[Union[List[Union[Decimal, 'Number', StrictBool, 'Boolean', str, 'Text', 'StructuredValue']], Decimal, 'Number', StrictBool, 'Boolean', str, 'Text', 'StructuredValue']] = Field(
        None,
        description="The value of the quantitative value or property value node. * For [[QuantitativeValue]]"
     "and [[MonetaryAmount]], the recommended type for values is 'Number'. * For [[PropertyValue]],"
     "it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'. * Use values from 0123456789"
     "(Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially"
     "similiar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to"
     "indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    maxValue: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The upper value of some characteristic or property.",
    )
    additionalProperty: Optional[Union[List[Union['PropertyValue', str]], 'PropertyValue', str]] = Field(
        None,
        description="A property-value pair representing an additional characteristics of the entitity,"
     "e.g. a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    valueReference: Optional[Union[List[Union[str, 'Text', 'PropertyValue', 'StructuredValue', 'MeasurementTypeEnumeration', 'QualitativeValue', 'Enumeration', 'QuantitativeValue', 'DefinedTerm']], str, 'Text', 'PropertyValue', 'StructuredValue', 'MeasurementTypeEnumeration', 'QualitativeValue', 'Enumeration', 'QuantitativeValue', 'DefinedTerm']] = Field(
        None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
