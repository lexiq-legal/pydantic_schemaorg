from pydantic import Field, StrictBool
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class PropertyValueSpecification(Intangible):
    """A Property value specification.

    See https://schema.org/PropertyValueSpecification.

    """

    multipleValues: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether multiple values are allowed for the property. Default is false.",
    )
    valueMaxLength: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Specifies the allowed range for number of characters in a literal value.",
    )
    readonlyValue: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
     "that also has a value makes it act similar to a \"hidden\" input in an HTML form.",
    )
    valueMinLength: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",
    )
    valuePattern: Optional[Union[List[str], str]] = Field(
        None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",
    )
    valueRequired: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Whether the property must be filled in to complete the action. Default is false.",
    )
    minValue: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The lower value of some characteristic or property.",
    )
    valueName: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
     "form encoding in a manner analogous to HTML's input@name.",
    )
    stepValue: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
     "of the value in a PropertyValueSpecification.",
    )
    maxValue: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The upper value of some characteristic or property.",
    )
    defaultValue: Optional[Union[List[Union[str, Thing]], Union[str, Thing]]] = Field(
        None,
        description="The default value of the input. For properties that expect a literal, the default is a"
     "literal value, for properties that expect an object, it's an ID reference to one of the"
     "current values.",
    )
    locals().update({"@type": Field("PropertyValueSpecification", const=True)})


PropertyValueSpecification.update_forward_refs()
