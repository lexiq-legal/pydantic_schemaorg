from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Series(Intangible):
    """A Series in schema.org is a group of related items, typically but not necessarily of the"
     "same kind. See also [[CreativeWorkSeries]], [[EventSeries]].

    See https://schema.org/Series.

    """
    type_: str = Field("Series", const=True, alias='@type')
    

Series.update_forward_refs()
