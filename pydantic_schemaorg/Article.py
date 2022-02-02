from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Article(CreativeWork):
    """An article, such as a news article or piece of investigative report. Newspapers and magazines"
     "have articles of many different types and this is intended to cover them all. See also"
     "[blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See: https://schema.org/Article
    Model depth: 3
    """
    type_: str = Field("Article", alias='@type')
    backstory: Optional[Union[List[Union[str, 'Text', 'CreativeWork']], str, 'Text', 'CreativeWork']] = Field(
        None,
        description="For an [[Article]], typically a [[NewsArticle]], the backstory property provides"
     "a textual summary giving a brief explanation of why and how an article was created. In"
     "a journalistic setting this could include information about reporting process, methods,"
     "interviews, data sources, etc.",
    )
    articleSection: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports,"
     "Lifestyle, etc.",
    )
    speakable: Optional[Union[List[Union[AnyUrl, 'URL', 'SpeakableSpecification', str]], AnyUrl, 'URL', 'SpeakableSpecification', str]] = Field(
        None,
        description="Indicates sections of a Web page that are particularly 'speakable' in the sense of being"
     "highlighted as being especially appropriate for text-to-speech conversion. Other"
     "sections of a page may also be usefully spoken in particular circumstances; the 'speakable'"
     "property serves to indicate the parts most likely to be generally useful for speech."
     "The *speakable* property can be repeated an arbitrary number of times, with three kinds"
     "of possible 'content-locator' values: 1.) *id-value* URL references - uses *id-value*"
     "of an element in the page being annotated. The simplest use of *speakable* has (potentially"
     "relative) URL values, referencing identified sections of the document concerned."
     "2.) CSS Selectors - addresses content in the annotated page, eg. via class attribute."
     "Use the [[cssSelector]] property. 3.) XPaths - addresses content via XPaths (assuming"
     "an XML view of the content). Use the [[xpath]] property. For more sophisticated markup"
     "of speakable sections beyond simple ID references, either CSS selectors or XPath expressions"
     "to pick out document section(s) as speakable. For this we define a supporting type, [[SpeakableSpecification]]"
     "which is defined to be a possible value of the *speakable* property.",
    )
    wordCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of words in the text of the Article.",
    )
    articleBody: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The actual body of the article.",
    )
    pageStart: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    pagination: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageEnd: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.SpeakableSpecification import SpeakableSpecification
    from pydantic_schemaorg.Integer import Integer
