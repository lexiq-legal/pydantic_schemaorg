from pydantic import Field
from datetime import date, datetime
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class DataFeedItem(Intangible):
    """A single item within a larger data feed.

    See https://schema.org/DataFeedItem.

    """

    dateDeleted: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The datetime the item was removed from the DataFeed.",
    )
    item: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.",
    )
    dateModified: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",
    )
    dateCreated: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    locals().update({"@type": Field("DataFeedItem", const=True)})


DataFeedItem.update_forward_refs()
