from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebContent(CreativeWork):
    """WebContent is a type representing all [[WebPage]], [[WebSite]] and [[WebPageElement]]"
     "content. It is sometimes the case that detailed distinctions between Web pages, sites"
     "and their parts is not always important or obvious. The [[WebContent]] type makes it"
     "easier to describe Web-addressable content without requiring such distinctions to"
     "always be stated. (The intent is that the existing types [[WebPage]], [[WebSite]] and"
     "[[WebPageElement]] will eventually be declared as subtypes of [[WebContent]]).

    See https://schema.org/WebContent.

    """
    type_: str = Field("WebContent", const=True, alias='@type')
    

WebContent.update_forward_refs()
