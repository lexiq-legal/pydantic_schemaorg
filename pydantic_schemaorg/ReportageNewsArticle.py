from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class ReportageNewsArticle(NewsArticle):
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing news"
     "articles which are the result of journalistic news reporting conventions. In practice"
     "many news publishers produce a wide variety of article types, many of which might be considered"
     "a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces,"
     "reviews, analysis, sponsored or satirical articles, or articles that combine several"
     "of these elements. The [[ReportageNewsArticle]] type is based on a stricter ideal for"
     "\"news\" as a work of journalism, with articles based on factual information either"
     "observed or verified by the author, or reported and verified from knowledgeable sources."
     "This often includes perspectives from multiple viewpoints on a particular issue (distinguishing"
     "news reports from public relations or propaganda). News reports in the [[ReportageNewsArticle]]"
     "sense de-emphasize the opinion of the author, with commentary and value judgements"
     "typically expressed elsewhere. A [[ReportageNewsArticle]] which goes deeper into"
     "analysis can also be marked with an additional type of [[AnalysisNewsArticle]].

    See https://schema.org/ReportageNewsArticle.

    """

    locals().update({"@type": Field("ReportageNewsArticle", const=True)})


ReportageNewsArticle.update_forward_refs()
