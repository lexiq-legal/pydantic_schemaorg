from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.GeoShape import GeoShape


class GeoCircle(GeoShape):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape"
     "it provides the simple textual property 'circle', but also allows the combination of"
     "postalCode alongside geoRadius. The center of the circle can be indicated via the 'geoMidpoint'"
     "property, or more approximately using 'address', 'postalCode'.

    See: https://schema.org/GeoCircle
    Model depth: 5
    """
    type_: str = Field("GeoCircle", alias='@type')
    geoMidpoint: Optional[Union[List[Union['GeoCoordinates', str]], 'GeoCoordinates', str]] = Field(
        None,
        description="Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle.",
    )
    geoRadius: Optional[Union[List[Union[Decimal, 'Number', str, 'Text', 'Distance']], Decimal, 'Number', str, 'Text', 'Distance']] = Field(
        None,
        description="Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise"
     "via Distance notation).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.GeoCoordinates import GeoCoordinates
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Distance import Distance
