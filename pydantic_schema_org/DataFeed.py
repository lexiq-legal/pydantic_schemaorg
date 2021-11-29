from pydantic import Field
from pydantic_schema_org.DataFeedItem import DataFeedItem
from pydantic_schema_org.Thing import Thing
from typing import Any, Optional, Union, List
from pydantic_schema_org.Dataset import Dataset


class DataFeed(Dataset):
    """A single feed providing structured information about one or more entities or topics.

    See https://schema.org/DataFeed.

    """

    dataFeedElement: Optional[Union[List[Union[str, DataFeedItem, Thing]], Union[str, DataFeedItem, Thing]]] = Field(
        None,
        description="An item within in a data feed. Data feeds may have many elements.",
    )
    locals().update({"@type": Field("DataFeed", const=True)})


DataFeed.update_forward_refs()
