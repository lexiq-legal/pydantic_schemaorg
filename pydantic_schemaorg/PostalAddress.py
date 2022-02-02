from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.ContactPoint import ContactPoint


class PostalAddress(ContactPoint):
    """The mailing address.

    See: https://schema.org/PostalAddress
    Model depth: 5
    """
    type_: str = Field("PostalAddress", alias='@type')
    postalCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The postal code. For example, 94043.",
    )
    streetAddress: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The street address. For example, 1600 Amphitheatre Pkwy.",
    )
    addressLocality: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The locality in which the street address is, and which is in the region. For example, Mountain"
     "View.",
    )
    postOfficeBoxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The post office box number for PO box addresses.",
    )
    addressCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    addressRegion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The region in which the locality is, and which is in the country. For example, California"
     "or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country)",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country
