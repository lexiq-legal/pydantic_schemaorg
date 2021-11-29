from pydantic import Field
from typing import Any, Union, List, Optional
from decimal import Decimal
from pydantic_schemaorg.PostalAddress import PostalAddress
from pydantic_schemaorg.Country import Country
from pydantic_schemaorg.StructuredValue import StructuredValue


class GeoCoordinates(StructuredValue):
    """The geographic coordinates of a place or event.

    See https://schema.org/GeoCoordinates.

    """

    postalCode: Optional[Union[List[str], str]] = Field(
        None,
        description="The postal code. For example, 94043.",
    )
    longitude: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    latitude: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    elevation: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."
     "Values may be of the form 'NUMBER UNIT_OF_MEASUREMENT' (e.g., '1,000 m', '3,200 ft')"
     "while numbers alone should be assumed to be a value in meters.",
    )
    address: Optional[Union[List[Union[str, PostalAddress]], Union[str, PostalAddress]]] = Field(
        None,
        description="Physical address of the item.",
    )
    addressCountry: Optional[Union[List[Union[str, Country]], Union[str, Country]]] = Field(
        None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    locals().update({"@type": Field("GeoCoordinates", const=True)})


GeoCoordinates.update_forward_refs()
