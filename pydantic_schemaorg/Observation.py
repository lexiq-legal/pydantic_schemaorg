from pydantic import Field
from typing import Any, Union, List, Optional
from datetime import datetime
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from pydantic_schemaorg.DataType import DataType
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

    See https://schema.org/Observation.

    """

    measuredProperty: Any = Field(
        None,
        description="The measuredProperty of an [[Observation]], either a schema.org property, a property"
     "from other RDF-compatible systems e.g. W3C RDF Data Cube, or schema.org extensions"
     "such as [GS1's](https://www.gs1.org/voc/?show=properties).",
    )
    observationDate: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The observationDate of an [[Observation]].",
    )
    marginOfError: Optional[Union[List[QuantitativeValue], QuantitativeValue]] = Field(
        None,
        description="A marginOfError for an [[Observation]].",
    )
    observedNode: Any = Field(
        None,
        description="The observedNode of an [[Observation]], often a [[StatisticalPopulation]].",
    )
    measuredValue: Optional[Union[List[DataType], DataType]] = Field(
        None,
        description="The measuredValue of an [[Observation]].",
    )
    locals().update({"@type": Field("Observation", const=True)})


Observation.update_forward_refs()
