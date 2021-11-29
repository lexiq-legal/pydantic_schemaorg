from pydantic import Field
from pydantic_schemaorg.DataFeed import DataFeed


class CompleteDataFeed(DataFeed):
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes"
     "content for every item currently in the feed. This is the equivalent of Atom's element"
     "as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005),"
     "For example (and as defined for Atom), when using data from a feed that represents a collection"
     "of items that varies over time (e.g. \"Top Twenty Records\") there is no need to have newer"
     "entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed,"
     "old entries can be safely discarded when the feed is refreshed, since we can assume the"
     "feed has provided descriptions for all current items.

    See https://schema.org/CompleteDataFeed.

    """

    locals().update({"@type": Field("CompleteDataFeed", const=True)})


CompleteDataFeed.update_forward_refs()
