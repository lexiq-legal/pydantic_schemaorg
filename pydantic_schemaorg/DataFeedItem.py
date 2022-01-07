from pydantic import Field
from datetime import datetime, date
from typing import List, Optional, Union
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class DataFeedItem(Intangible):
    """A single item within a larger data feed.

    See https://schema.org/DataFeedItem.

    """
    type_: str = Field("DataFeedItem", const=True, alias='@type')
    dateDeleted: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The datetime the item was removed from the DataFeed.",
    )
    item: Optional[Union[List[Union[Thing, str]], Union[Thing, str]]] = Field(
        None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.",
    )
    dateModified: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",
    )
    dateCreated: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    

DataFeedItem.update_forward_refs()
