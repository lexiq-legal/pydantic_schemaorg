from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class BookSeries(CreativeWorkSeries):
    """A series of books. Included books can be indicated with the hasPart property.

    See https://schema.org/BookSeries.

    """

    locals().update({"@type": Field("BookSeries", const=True)})


BookSeries.update_forward_refs()
