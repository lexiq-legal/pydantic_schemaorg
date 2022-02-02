from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Dataset import Dataset


class DataFeed(Dataset):
    """A single feed providing structured information about one or more entities or topics.

    See: https://schema.org/DataFeed
    Model depth: 4
    """
    type_: str = Field("DataFeed", alias='@type')
    dataFeedElement: Optional[Union[List[Union[str, 'Text', 'Thing', 'DataFeedItem']], str, 'Text', 'Thing', 'DataFeedItem']] = Field(
        None,
        description="An item within in a data feed. Data feeds may have many elements.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.DataFeedItem import DataFeedItem
