from pydantic import AnyUrl, Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import List, Optional, Union
from pydantic_schemaorg.QualitativeValue import QualitativeValue
from pydantic_schemaorg.StructuredValue import StructuredValue


class EngineSpecification(StructuredValue):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented"
     "by multiple engine specification entities.

    See https://schema.org/EngineSpecification.

    """
    type_: str = Field("EngineSpecification", const=True, alias='@type')
    torque: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The torque (turning force) of the vehicle's engine. Typical unit code(s): NU for newton"
     "metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch * Note 1: You"
     "can link to information about how the given value has been determined (e.g. reference"
     "RPM) using the [[valueReference]] property. * Note 2: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    engineType: Optional[Union[List[Union[AnyUrl, str, QualitativeValue]], Union[AnyUrl, str, QualitativeValue]]] = Field(
        None,
        description="The type of engine or engines powering the vehicle.",
    )
    fuelType: Optional[Union[List[Union[AnyUrl, str, QualitativeValue]], Union[AnyUrl, str, QualitativeValue]]] = Field(
        None,
        description="The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only"
     "one engine, this property can be attached directly to the vehicle.",
    )
    engineDisplacement: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The volume swept by all of the pistons inside the cylinders of an internal combustion"
     "engine in a single movement. Typical unit code(s): CMQ for cubic centimeter, LTR for"
     "liters, INQ for cubic inches * Note 1: You can link to information about how the given value"
     "has been determined using the [[valueReference]] property. * Note 2: You can use [[minValue]]"
     "and [[maxValue]] to indicate ranges.",
    )
    enginePower: Optional[Union[List[Union[QuantitativeValue, str]], Union[QuantitativeValue, str]]] = Field(
        None,
        description="The power of the vehicle's engine. Typical unit code(s): KWT for kilowatt, BHP for brake"
     "horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W) * Note 1: There are"
     "many different ways of measuring an engine's power. For an overview, see [http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes)."
     "* Note 2: You can link to information about how the given value has been determined using"
     "the [[valueReference]] property. * Note 3: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    

EngineSpecification.update_forward_refs()
