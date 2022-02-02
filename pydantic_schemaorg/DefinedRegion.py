from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class DefinedRegion(StructuredValue):
    """A DefinedRegion is a geographic area defined by potentially arbitrary (rather than"
     "political, administrative or natural geographical) criteria. Properties are provided"
     "for defining a region by reference to sets of postal codes. Examples: a delivery destination"
     "when shopping. Region where regional pricing is configured. Requirement 1: Country:"
     "US States: \"NY\", \"CA\" Requirement 2: Country: US PostalCode Set: { [94000-94585],"
     "[97000, 97999], [13000, 13599]} { [12345, 12345], [78945, 78945], } Region = state,"
     "canton, prefecture, autonomous community...

    See: https://schema.org/DefinedRegion
    Model depth: 4
    """
    type_: str = Field("DefinedRegion", alias='@type')
    postalCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The postal code. For example, 94043.",
    )
    postalCodePrefix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A defined range of postal codes indicated by a common textual prefix. Used for non-numeric"
     "systems such as UK.",
    )
    addressCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    postalCodeRange: Optional[Union[List[Union['PostalCodeRangeSpecification', str]], 'PostalCodeRangeSpecification', str]] = Field(
        None,
        description="A defined range of postal codes.",
    )
    addressRegion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The region in which the locality is, and which is in the country. For example, California"
     "or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.PostalCodeRangeSpecification import PostalCodeRangeSpecification
