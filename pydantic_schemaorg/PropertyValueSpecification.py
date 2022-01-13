from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class PropertyValueSpecification(Intangible):
    """A Property value specification.

    See: https://schema.org/PropertyValueSpecification
    Model depth: 3
    """

    type_: str = Field("PropertyValueSpecification", const=True, alias="@type")
    multipleValues: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="Whether multiple values are allowed for the property. Default is false.",
    )
    valueMaxLength: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="Specifies the allowed range for number of characters in a literal value.",
    )
    readonlyValue: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
        'that also has a value makes it act similar to a "hidden" input in an HTML form.',
    )
    valueMinLength: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",
    )
    valuePattern: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",
    )
    valueRequired: "Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]]" = Field(
        None,
        description="Whether the property must be filled in to complete the action. Default is false.",
    )
    minValue: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The lower value of some characteristic or property.",
    )
    valueName: "Optional[Union[List[str], str]]" = Field(
        None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
        "form encoding in a manner analogous to HTML's input@name.",
    )
    stepValue: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
        "of the value in a PropertyValueSpecification.",
    )
    maxValue: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The upper value of some characteristic or property.",
    )
    defaultValue: "Optional[Union[List[Union[str, Thing]], Union[str, Thing]]]" = Field(
        None,
        description="The default value of the input. For properties that expect a literal, the default is a"
        "literal value, for properties that expect an object, it's an ID reference to one of the"
        "current values.",
    )


if TYPE_CHECKING:

    from pydantic import StrictBool

    from decimal import Decimal

    from pydantic_schemaorg.Thing import Thing

    PropertyValueSpecification.update_forward_refs()
