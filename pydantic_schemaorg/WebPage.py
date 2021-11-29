from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from datetime import date
from pydantic_schemaorg.Specialty import Specialty
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebPage(CreativeWork):
    """A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so"
     "the various properties about that webpage, such as <code>breadcrumb</code> may be"
     "used. We recommend explicit declaration if these properties are specified, but if they"
     "are found outside of an itemscope, they will be assumed to be about the page.

    See https://schema.org/WebPage.

    """

    significantLink: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="One of the more significant URLs on the page. Typically, these are the non-navigation"
     "links that are clicked on the most.",
    )
    speakable: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
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
    significantLinks: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="The most significant URLs on the page. Typically, these are the non-navigation links"
     "that are clicked on the most.",
    )
    relatedLink: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A link related to this web page, for example to other related web pages.",
    )
    reviewedBy: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="People or organizations that have reviewed the content on this web page for accuracy"
     "and/or completeness.",
    )
    breadcrumb: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A set of links that can help a user understand and navigate a website hierarchy.",
    )
    primaryImageOfPage: Any = Field(
        None,
        description="Indicates the main image on the page.",
    )
    lastReviewed: Optional[Union[List[date], date]] = Field(
        None,
        description="Date on which the content on this web page was last reviewed for accuracy and/or completeness.",
    )
    mainContentOfPage: Any = Field(
        None,
        description="Indicates if this web page element is the main subject of the page.",
    )
    specialty: Optional[Union[List[Specialty], Specialty]] = Field(
        None,
        description="One of the domain specialities to which this web page's content applies.",
    )
    locals().update({"@type": Field("WebPage", const=True)})


WebPage.update_forward_refs()
