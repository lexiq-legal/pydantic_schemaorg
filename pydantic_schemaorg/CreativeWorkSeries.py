from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.Series import Series
from pydantic_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeries(Series, CreativeWork):
    """A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily"
     "of the same kind. CreativeWorkSeries are usually organized into some order, often chronological."
     "Unlike [[ItemList]] which is a general purpose data structure for lists of things, the"
     "emphasis with CreativeWorkSeries is on published materials (written e.g. books and"
     "periodicals, or media such as tv, radio and games). Specific subtypes are available"
     "for describing [[TVSeries]], [[RadioSeries]], [[MovieSeries]], [[BookSeries]],"
     "[[Periodical]] and [[VideoGameSeries]]. In each case, the [[hasPart]] / [[isPartOf]]"
     "properties can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries"
     "type serves largely just to organize these more specific and practical subtypes. It"
     "is common for properties applicable to an item from the series to be usefully applied"
     "to the containing group. Schema.org attempts to anticipate some of these cases, but"
     "publishers should be free to apply properties of the series parts to the series as a whole"
     "wherever they seem appropriate.

    See: https://schema.org/CreativeWorkSeries
    Model depth: 3
    """
    type_: str = Field("CreativeWorkSeries", alias='@type')
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    issn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
