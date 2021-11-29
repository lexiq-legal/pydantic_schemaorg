from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class BackgroundNewsArticle(NewsArticle):
    """A [[NewsArticle]] providing historical context, definition and detail on a specific"
     "topic (aka \"explainer\" or \"backgrounder\"). For example, an in-depth article or"
     "frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document"
     "on topics such as Climate Change or the European Union. Other kinds of background material"
     "from a non-news setting are often described using [[Book]] or [[Article]], in particular"
     "[[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education"
     "perspective.

    See https://schema.org/BackgroundNewsArticle.

    """

    locals().update({"@type": Field("BackgroundNewsArticle", const=True)})


BackgroundNewsArticle.update_forward_refs()
