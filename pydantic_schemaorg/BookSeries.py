from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """A series of books. Included books can be indicated with the hasPart property.

    See https://schema.org/BookSeries.

    """
    type_: str = Field("BookSeries", const=True, alias='@type')
    

BookSeries.update_forward_refs()
