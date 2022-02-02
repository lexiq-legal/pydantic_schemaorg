from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Observation(Intangible):
    """Instances of the class [[Observation]] are used to specify observations about an entity"
     "(which may or may not be an instance of a [[StatisticalPopulation]]), at a particular"
     "time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]],"
     "[[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]]"
     "properties can, but need not always, be W3C RDF Data Cube \"measure properties\", as"
     "in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example))."
     "See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html)"
     "overview for more details.

    See: https://schema.org/Observation
    Model depth: 3
    """
    type_: str = Field("Observation", alias='@type')
    measuredProperty: Optional[Union[List[Union['Property', str]], 'Property', str]] = Field(
        None,
        description="The measuredProperty of an [[Observation]], either a schema.org property, a property"
     "from other RDF-compatible systems e.g. W3C RDF Data Cube, or schema.org extensions"
     "such as [GS1's](https://www.gs1.org/voc/?show=properties).",
    )
    observationDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The observationDate of an [[Observation]].",
    )
    marginOfError: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="A marginOfError for an [[Observation]].",
    )
    observedNode: Optional[Union[List[Union['StatisticalPopulation', str]], 'StatisticalPopulation', str]] = Field(
        None,
        description="The observedNode of an [[Observation]], often a [[StatisticalPopulation]].",
    )
    measuredValue: Optional[Union[List[Union['DataType', str]], 'DataType', str]] = Field(
        None,
        description="The measuredValue of an [[Observation]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.StatisticalPopulation import StatisticalPopulation
    from pydantic_schemaorg.DataType import DataType
