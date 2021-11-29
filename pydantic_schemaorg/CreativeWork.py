from pydantic import Field, AnyUrl, StrictBool
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from datetime import date, datetime
from pydantic_schemaorg.Organization import Organization
from decimal import Decimal


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies, photographs, software"
     "programs, etc.

    See https://schema.org/CreativeWork.

    """

    pattern: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    creditText: Optional[Union[List[str], str]] = Field(
        None,
        description="Text that can be used to credit person(s) and/or organization(s) associated with a published"
     "Creative Work.",
    )
    about: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The subject matter of the content.",
    )
    text: Optional[Union[List[str], str]] = Field(
        None,
        description="The textual content of this CreativeWork.",
    )
    character: Any = Field(
        None,
        description="Fictional person connected with a creative work.",
    )
    offers: Any = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    locationCreated: Any = Field(
        None,
        description="The location where the CreativeWork was created, which may not be the same as the location"
     "depicted in the CreativeWork.",
    )
    isBasedOnUrl: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A resource that was used in the creation of this resource. This term can be repeated for"
     "multiple sources. For example, http://example.com/great-multiplication-intro.html.",
    )
    isPartOf: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is"
     "part of.",
    )
    materialExtent: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The quantity of the materials being described or an expression of the physical space"
     "they occupy.",
    )
    contentReferenceTime: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The specific time described by a creative work, for works (e.g. articles, video objects"
     "etc.) that emphasise a particular moment within an Event.",
    )
    maintainer: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other"
     "[[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions"
     "to, and/or publication of, some (typically complex) artifact. It is common for distributions"
     "of software and data to be based on \"upstream\" sources. When [[maintainer]] is applied"
     "to a specific version of something e.g. a particular version or packaging of a [[Dataset]],"
     "it is always possible that the upstream source has a different maintainer. The [[isBasedOn]]"
     "property can be used to indicate such relationships between datasets to make the different"
     "maintenance roles clear. Similarly in the case of software, a package may have dedicated"
     "maintainers working on integration into software distributions such as Ubuntu, as"
     "well as upstream maintainers of the underlying work.",
    )
    typicalAgeRange: Optional[Union[List[str], str]] = Field(
        None,
        description="The typical expected age range, e.g. '7-9', '11-'.",
    )
    author: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",
    )
    funder: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    expires: Optional[Union[List[date], date]] = Field(
        None,
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]]"
     "or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]]"
     "fact check whose publisher wants to indicate that it may no longer be relevant (or helpful"
     "to highlight) after some date.",
    )
    genre: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    workTranslation: Any = Field(
        None,
        description="A work that is a translation of the content of this work. e.g. 西遊記 has an English workTranslation"
     "“Journey to the West”,a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese"
     "translation Tây du ký bình khảo.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[str], str]] = Field(
        None,
        description="An award won by or for this item.",
    )
    temporalCoverage: Optional[Union[List[Union[datetime, AnyUrl, str]], Union[datetime, AnyUrl, str]]] = Field(
        None,
        description="The temporalCoverage of a CreativeWork indicates the period that the content applies"
     "to, i.e. that it describes, either as a DateTime or as a textual string indicating a time"
     "period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)."
     "In the case of a Dataset it will typically indicate the relevant time period in a precise"
     "notation (e.g. for a 2011 census dataset, the year 2011 would be written \"2011/2012\")."
     "Other forms of content e.g. ScholarlyArticle, Book, TVSeries or TVEpisode may indicate"
     "their temporalCoverage in broader terms - textually or via well-known URL. Written"
     "works such as books may sometimes have precise temporal coverage too, e.g. a work set"
     "in 1939 - 1945 can be indicated in ISO 8601 interval format format via \"1939/1945\"."
     "Open-ended date ranges can be written with \"..\" in place of the end date. For example,"
     "\"2015-11/..\" indicates a range beginning in November 2015 and with no specified final"
     "date. This is tentative and might be updated in future when ISO 8601 is officially updated.",
    )
    hasPart: Any = Field(
        None,
        description="Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some"
     "sense).",
    )
    accessibilitySummary: Optional[Union[List[str], str]] = Field(
        None,
        description="A human-readable summary of specific accessibility features or deficiencies, consistent"
     "with the other accessibility metadata but expressing subtleties such as \"short descriptions"
     "are present but long descriptions will be needed for non-visual users\" or \"short descriptions"
     "are present and no long descriptions are needed.\"",
    )
    accessModeSufficient: Any = Field(
        None,
        description="A list of single or combined accessModes that are sufficient to understand all the intellectual"
     "content of a resource. Expected values include: auditory, tactile, textual, visual.",
    )
    headline: Optional[Union[List[str], str]] = Field(
        None,
        description="Headline of the article.",
    )
    educationalAlignment: Any = Field(
        None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",
    )
    publishingPrinciples: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual e.g. a [[Person]] writing"
     "a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies."
     "When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those"
     "of the party primarily responsible for the creation of the [[CreativeWork]]. While"
     "such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    comment: Any = Field(
        None,
        description="Comments, typically from users.",
    )
    audio: Any = Field(
        None,
        description="An embedded audio object.",
    )
    video: Any = Field(
        None,
        description="An embedded video object.",
    )
    sourceOrganization: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The Organization on whose behalf the creator was working.",
    )
    translator: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",
    )
    position: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The position of an item in a series or sequence of items.",
    )
    translationOfWork: Any = Field(
        None,
        description="The work that this work has been translated from. e.g. 物种起源 is a translationOf “On the"
     "Origin of Species”",
    )
    isBasedOn: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A resource from which this work is derived or from which it is a modification or adaption.",
    )
    schemaVersion: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Indicates (by URL or string) a particular version of a schema used in some CreativeWork."
     "This property was created primarily to indicate the use of a specific schema.org release,"
     "e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```."
     "There may be situations in which other schemas might usefully be referenced this way,"
     "e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/```"
     "but this has not been carefully explored in the community.",
    )
    countryOfOrigin: Any = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    editEIDR: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]]"
     "representing a specific edit / edition for a work of film or television. For example,"
     "the motion picture known as \"Ghostbusters\" whose [[titleEIDR]] is \"10.5240/7EC7-228A-510A-053E-CBB8-J\","
     "has several edits e.g. \"10.5240/1F2A-E1C5-680A-14C6-E76B-I\" and \"10.5240/8A35-3BEE-6497-5D12-9E4F-3\"."
     "Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and"
     "their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general"
     "description), or alongside [[editEIDR]] for a more edit-specific description.",
    )
    sdPublisher: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="Indicates the party responsible for generating and publishing the current structured"
     "data markup, typically in cases where the structured data is derived automatically"
     "from existing published content but published on a different site. For example, student"
     "projects and open data initiatives often re-publish existing content with more explicitly"
     "structured metadata. The [[sdPublisher]] property helps make such practices more"
     "explicit.",
    )
    license: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A license document that applies to this content, typically indicated by URL.",
    )
    interactionStatistic: Any = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    accessibilityFeature: Optional[Union[List[str], str]] = Field(
        None,
        description="Content features of the resource, such as accessible media, alternatives and supported"
     "enhancements for accessibility ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    mentions: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="Indicates that the CreativeWork contains a reference to, but is not necessarily about"
     "a concept.",
    )
    temporal: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="The \"temporal\" property can be used in cases where more specific properties (e.g."
     "[[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]])"
     "are not known to be appropriate.",
    )
    usageInfo: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]."
     "This property is applicable both to works that are freely available and to those that"
     "require payment or other transactions. It can reference additional information e.g."
     "community expectations on preferred linking and citation conventions, as well as purchasing"
     "details. For something that can be commercially licensed, usageInfo can provide detailed,"
     "resource-specific information about licensing options. This property can be used"
     "alongside the license property which indicates license(s) applicable to some piece"
     "of content. The usageInfo property can provide information about other licensing options,"
     "e.g. acquiring commercial usage rights for an image that is also available under non-commercial"
     "creative commons licenses.",
    )
    creativeWorkStatus: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The status of a creative work in terms of its stage in a lifecycle. Example terms include"
     "Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for"
     "the stages of their publication lifecycle.",
    )
    publisher: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The publisher of the creative work.",
    )
    releasedEvent: Any = Field(
        None,
        description="The place and time the release was issued, expressed as a PublicationEvent.",
    )
    alternativeHeadline: Optional[Union[List[str], str]] = Field(
        None,
        description="A secondary title of the CreativeWork.",
    )
    sdLicense: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A license document that applies to this structured data, typically indicated by URL.",
    )
    accountablePerson: Any = Field(
        None,
        description="Specifies the Person that is legally accountable for the CreativeWork.",
    )
    copyrightNotice: Optional[Union[List[str], str]] = Field(
        None,
        description="Text of a notice appropriate for describing the copyright aspects of this Creative Work,"
     "ideally indicating the owner of the copyright for the Work.",
    )
    teaches: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",
    )
    exampleOfWork: Any = Field(
        None,
        description="A creative work that this work is an example/instance/realization/derivation of.",
    )
    recordedAt: Any = Field(
        None,
        description="The Event where the CreativeWork was recorded. The CreativeWork may capture all or part"
     "of the event.",
    )
    conditionsOfAccess: Optional[Union[List[str], str]] = Field(
        None,
        description="Conditions that affect the availability of, or method(s) of access to, an item. Typically"
     "used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]."
     "This property is not suitable for use as a general Web access control mechanism. It is"
     "expressed only in natural language. For example \"Available by appointment from the"
     "Reading Room\" or \"Accessible only from logged-in accounts \".",
    )
    workExample: Any = Field(
        None,
        description="Example/instance/realization/derivation of the concept of this creative work. eg."
     "The paperback edition, first edition, or eBook.",
    )
    size: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    accessibilityHazard: Optional[Union[List[str], str]] = Field(
        None,
        description="A characteristic of the described resource that is physiologically dangerous to some"
     "users. Related to WCAG 2.0 guideline 2.3 ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    copyrightYear: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The year during which the claimed copyright for the CreativeWork was first asserted.",
    )
    encodings: Any = Field(
        None,
        description="A media object that encodes this CreativeWork.",
    )
    creator: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    accessMode: Optional[Union[List[str], str]] = Field(
        None,
        description="The human sensory perceptual system or cognitive faculty through which a person may"
     "process or perceive information. Expected values include: auditory, tactile, textual,"
     "visual, colorDependent, chartOnVisual, chemOnVisual, diagramOnVisual, mathOnVisual,"
     "musicOnVisual, textOnVisual.",
    )
    abstract: Optional[Union[List[str], str]] = Field(
        None,
        description="An abstract is a short description that summarizes a [[CreativeWork]].",
    )
    thumbnailUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A thumbnail image relevant to the Thing.",
    )
    acquireLicensePage: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Indicates a page documenting how licenses can be purchased or otherwise acquired, for"
     "the current item.",
    )
    contentRating: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Official rating of a piece of content&#x2014;for example,'MPAA PG-13'.",
    )
    awards: Optional[Union[List[str], str]] = Field(
        None,
        description="Awards won by or for this item.",
    )
    isFamilyFriendly: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether this content is family friendly.",
    )
    editor: Any = Field(
        None,
        description="Specifies the Person who edited the CreativeWork.",
    )
    datePublished: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="Date of first broadcast/publication.",
    )
    educationalLevel: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    assesses: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",
    )
    mainEntity: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="Indicates the primary entity described in some page or other CreativeWork.",
    )
    correction: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]],"
     "textually or in another document.",
    )
    timeRequired: Any = Field(
        None,
        description="Approximate or typical time it takes to work with or through this learning resource for"
     "the typical intended target audience, e.g. 'PT30M', 'PT1H25M'.",
    )
    keywords: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Keywords or tags used to describe this content. Multiple entries in a keywords list are"
     "typically delimited by commas.",
    )
    audience: Any = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    sponsor: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    educationalUse: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",
    )
    sdDatePublished: Optional[Union[List[date], date]] = Field(
        None,
        description="Indicates the date on which the current structured data was generated / published. Typically"
     "used alongside [[sdPublisher]]",
    )
    spatialCoverage: Any = Field(
        None,
        description="The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of"
     "the content. It is a subproperty of contentLocation intended primarily for more technical"
     "and detailed materials. For example with a Dataset, it indicates areas that the dataset"
     "describes: a dataset of New York weather would have spatialCoverage which was the place:"
     "the state of New York.",
    )
    material: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    publication: Any = Field(
        None,
        description="A publication event associated with the item.",
    )
    encodingFormat: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)"
     "and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types))"
     "e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.)."
     "In cases where a [[CreativeWork]] has several media type representations, [[encoding]]"
     "can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]]"
     "information. Unregistered or niche encoding and file formats can be indicated instead"
     "via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",
    )
    inLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    dateModified: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",
    )
    reviews: Any = Field(
        None,
        description="Review of the item.",
    )
    dateCreated: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    associatedMedia: Any = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    interpretedAsClaim: Any = Field(
        None,
        description="Used to indicate a specific claim contained, implied, translated or refined from the"
     "content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can"
     "be indicated using [[claimInterpreter]].",
    )
    review: Any = Field(
        None,
        description="A review of the item.",
    )
    publisherImprint: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The publishing division which published the comic.",
    )
    accessibilityAPI: Optional[Union[List[str], str]] = Field(
        None,
        description="Indicates that the resource is compatible with the referenced accessibility API ([WebSchemas"
     "wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    version: Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]] = Field(
        None,
        description="The version of the CreativeWork embodied by a specified resource.",
    )
    learningResourceType: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",
    )
    discussionUrl: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None,
        description="A link to the page containing the comments of the CreativeWork.",
    )
    provider: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    fileFormat: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml))"
     "of the content e.g. application/zip of a SoftwareApplication binary. In cases where"
     "a CreativeWork has several media type representations, 'encoding' can be used to indicate"
     "each MediaObject alongside particular fileFormat information. Unregistered or niche"
     "file formats can be indicated instead via the most appropriate URL, e.g. defining Web"
     "page or a Wikipedia entry.",
    )
    producer: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The person or organization who produced the work (e.g. music album, movie, tv/radio"
     "series etc.).",
    )
    citation: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A citation or reference to another creative work, such as another publication, web page,"
     "scholarly article, etc.",
    )
    archivedAt: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case"
     "of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible,"
     "but be archived by archival, journalistic, activist, or law enforcement organizations."
     "In such cases, the referenced page may not directly publish the content.",
    )
    encoding: Any = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.",
    )
    interactivityType: Optional[Union[List[str], str]] = Field(
        None,
        description="The predominant mode of learning supported by the learning resource. Acceptable values"
     "are 'active', 'expositive', or 'mixed'.",
    )
    spatial: Any = Field(
        None,
        description="The \"spatial\" property can be used in cases when more specific properties (e.g. [[locationCreated]],"
     "[[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.",
    )
    contentLocation: Any = Field(
        None,
        description="The location depicted or described in the content. For example, the location in a photograph"
     "or painting.",
    )
    copyrightHolder: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The party holding the legal copyright to the CreativeWork.",
    )
    contributor: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="A secondary contributor to the CreativeWork or Event.",
    )
    isAccessibleForFree: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    accessibilityControl: Optional[Union[List[str], str]] = Field(
        None,
        description="Identifies input methods that are sufficient to fully control the described resource"
     "([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    commentCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of comments this CreativeWork (e.g. Article, Question or Answer) has received."
     "This is most applicable to works published in Web sites with commenting system; additional"
     "comments may exist elsewhere.",
    )
    locals().update({"@type": Field("CreativeWork", const=True)})


CreativeWork.update_forward_refs()
