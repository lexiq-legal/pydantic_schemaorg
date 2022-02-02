from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool, AnyUrl
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class CreativeWork(Thing):
    """The most generic kind of creative work, including books, movies, photographs, software"
     "programs, etc.

    See: https://schema.org/CreativeWork
    Model depth: 2
    """
    type_: str = Field("CreativeWork", alias='@type')
    pattern: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    creditText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Text that can be used to credit person(s) and/or organization(s) associated with a published"
     "Creative Work.",
    )
    about: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The subject matter of the content.",
    )
    text: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The textual content of this CreativeWork.",
    )
    character: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Fictional person connected with a creative work.",
    )
    offers: Optional[Union[List[Union['Demand', 'Offer', str]], 'Demand', 'Offer', str]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    locationCreated: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="The location where the CreativeWork was created, which may not be the same as the location"
     "depicted in the CreativeWork.",
    )
    isBasedOnUrl: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', 'Product', str]], AnyUrl, 'URL', 'CreativeWork', 'Product', str]] = Field(
        None,
        description="A resource that was used in the creation of this resource. This term can be repeated for"
     "multiple sources. For example, http://example.com/great-multiplication-intro.html.",
    )
    isPartOf: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is"
     "part of.",
    )
    materialExtent: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,
        description="The quantity of the materials being described or an expression of the physical space"
     "they occupy.",
    )
    contentReferenceTime: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The specific time described by a creative work, for works (e.g. articles, video objects"
     "etc.) that emphasise a particular moment within an Event.",
    )
    maintainer: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
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
    typicalAgeRange: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The typical expected age range, e.g. '7-9', '11-'.",
    )
    author: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The author of this content or rating. Please note that author is special in that HTML 5"
     "provides a special mechanism for indicating authorship via the rel tag. That is equivalent"
     "to this and may be used interchangeably.",
    )
    funder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    expires: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]]"
     "or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]]"
     "fact check whose publisher wants to indicate that it may no longer be relevant (or helpful"
     "to highlight) after some date.",
    )
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    workTranslation: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="A work that is a translation of the content of this work. e.g. 西遊記 has an English workTranslation"
     "“Journey to the West”,a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese"
     "translation Tây du ký bình khảo.",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An award won by or for this item.",
    )
    temporalCoverage: Optional[Union[List[Union[ISO8601Date, 'DateTime', AnyUrl, 'URL', str, 'Text']], ISO8601Date, 'DateTime', AnyUrl, 'URL', str, 'Text']] = Field(
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
    hasPart: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some"
     "sense).",
    )
    accessibilitySummary: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A human-readable summary of specific accessibility features or deficiencies, consistent"
     "with the other accessibility metadata but expressing subtleties such as \"short descriptions"
     "are present but long descriptions will be needed for non-visual users\" or \"short descriptions"
     "are present and no long descriptions are needed.\"",
    )
    accessModeSufficient: Optional[Union[List[Union['ItemList', str]], 'ItemList', str]] = Field(
        None,
        description="A list of single or combined accessModes that are sufficient to understand all the intellectual"
     "content of a resource. Expected values include: auditory, tactile, textual, visual.",
    )
    headline: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Headline of the article.",
    )
    educationalAlignment: Optional[Union[List[Union['AlignmentObject', str]], 'AlignmentObject', str]] = Field(
        None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual e.g. a [[Person]] writing"
     "a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies."
     "When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those"
     "of the party primarily responsible for the creation of the [[CreativeWork]]. While"
     "such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    comment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        None,
        description="Comments, typically from users.",
    )
    audio: Optional[Union[List[Union['AudioObject', 'MusicRecording', 'Clip', str]], 'AudioObject', 'MusicRecording', 'Clip', str]] = Field(
        None,
        description="An embedded audio object.",
    )
    video: Optional[Union[List[Union['Clip', 'VideoObject', str]], 'Clip', 'VideoObject', str]] = Field(
        None,
        description="An embedded video object.",
    )
    sourceOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The Organization on whose behalf the creator was working.",
    )
    translator: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="Organization or person who adapts a creative work to different languages, regional"
     "differences and technical requirements of a target market, or that translates during"
     "some event.",
    )
    position: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="The position of an item in a series or sequence of items.",
    )
    translationOfWork: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="The work that this work has been translated from. e.g. 物种起源 is a translationOf “On the"
     "Origin of Species”",
    )
    isBasedOn: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', 'Product', str]], AnyUrl, 'URL', 'CreativeWork', 'Product', str]] = Field(
        None,
        description="A resource from which this work is derived or from which it is a modification or adaption.",
    )
    schemaVersion: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Indicates (by URL or string) a particular version of a schema used in some CreativeWork."
     "This property was created primarily to indicate the use of a specific schema.org release,"
     "e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```."
     "There may be situations in which other schemas might usefully be referenced this way,"
     "e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/```"
     "but this has not been carefully explored in the community.",
    )
    countryOfOrigin: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    editEIDR: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]]"
     "representing a specific edit / edition for a work of film or television. For example,"
     "the motion picture known as \"Ghostbusters\" whose [[titleEIDR]] is \"10.5240/7EC7-228A-510A-053E-CBB8-J\","
     "has several edits e.g. \"10.5240/1F2A-E1C5-680A-14C6-E76B-I\" and \"10.5240/8A35-3BEE-6497-5D12-9E4F-3\"."
     "Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and"
     "their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general"
     "description), or alongside [[editEIDR]] for a more edit-specific description.",
    )
    sdPublisher: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="Indicates the party responsible for generating and publishing the current structured"
     "data markup, typically in cases where the structured data is derived automatically"
     "from existing published content but published on a different site. For example, student"
     "projects and open data initiatives often re-publish existing content with more explicitly"
     "structured metadata. The [[sdPublisher]] property helps make such practices more"
     "explicit.",
    )
    license: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="A license document that applies to this content, typically indicated by URL.",
    )
    interactionStatistic: Optional[Union[List[Union['InteractionCounter', str]], 'InteractionCounter', str]] = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    accessibilityFeature: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Content features of the resource, such as accessible media, alternatives and supported"
     "enhancements for accessibility ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    mentions: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="Indicates that the CreativeWork contains a reference to, but is not necessarily about"
     "a concept.",
    )
    temporal: Optional[Union[List[Union[ISO8601Date, 'DateTime', str, 'Text']], ISO8601Date, 'DateTime', str, 'Text']] = Field(
        None,
        description="The \"temporal\" property can be used in cases where more specific properties (e.g."
     "[[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]])"
     "are not known to be appropriate.",
    )
    usageInfo: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
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
    creativeWorkStatus: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The status of a creative work in terms of its stage in a lifecycle. Example terms include"
     "Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for"
     "the stages of their publication lifecycle.",
    )
    publisher: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The publisher of the creative work.",
    )
    releasedEvent: Optional[Union[List[Union['PublicationEvent', str]], 'PublicationEvent', str]] = Field(
        None,
        description="The place and time the release was issued, expressed as a PublicationEvent.",
    )
    alternativeHeadline: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A secondary title of the CreativeWork.",
    )
    sdLicense: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="A license document that applies to this structured data, typically indicated by URL.",
    )
    accountablePerson: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Specifies the Person that is legally accountable for the CreativeWork.",
    )
    copyrightNotice: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Text of a notice appropriate for describing the copyright aspects of this Creative Work,"
     "ideally indicating the owner of the copyright for the Work.",
    )
    teaches: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",
    )
    exampleOfWork: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="A creative work that this work is an example/instance/realization/derivation of.",
    )
    recordedAt: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="The Event where the CreativeWork was recorded. The CreativeWork may capture all or part"
     "of the event.",
    )
    conditionsOfAccess: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Conditions that affect the availability of, or method(s) of access to, an item. Typically"
     "used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]."
     "This property is not suitable for use as a general Web access control mechanism. It is"
     "expressed only in natural language. For example \"Available by appointment from the"
     "Reading Room\" or \"Accessible only from logged-in accounts \".",
    )
    workExample: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="Example/instance/realization/derivation of the concept of this creative work. eg."
     "The paperback edition, first edition, or eBook.",
    )
    size: Optional[Union[List[Union[str, 'Text', 'SizeSpecification', 'QuantitativeValue', 'DefinedTerm']], str, 'Text', 'SizeSpecification', 'QuantitativeValue', 'DefinedTerm']] = Field(
        None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    accessibilityHazard: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A characteristic of the described resource that is physiologically dangerous to some"
     "users. Related to WCAG 2.0 guideline 2.3 ([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    copyrightYear: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The year during which the claimed copyright for the CreativeWork was first asserted.",
    )
    encodings: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        None,
        description="A media object that encodes this CreativeWork.",
    )
    creator: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    accessMode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The human sensory perceptual system or cognitive faculty through which a person may"
     "process or perceive information. Expected values include: auditory, tactile, textual,"
     "visual, colorDependent, chartOnVisual, chemOnVisual, diagramOnVisual, mathOnVisual,"
     "musicOnVisual, textOnVisual.",
    )
    abstract: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An abstract is a short description that summarizes a [[CreativeWork]].",
    )
    thumbnailUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="A thumbnail image relevant to the Thing.",
    )
    acquireLicensePage: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="Indicates a page documenting how licenses can be purchased or otherwise acquired, for"
     "the current item.",
    )
    contentRating: Optional[Union[List[Union[str, 'Text', 'Rating']], str, 'Text', 'Rating']] = Field(
        None,
        description="Official rating of a piece of content&#x2014;for example,'MPAA PG-13'.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Awards won by or for this item.",
    )
    isFamilyFriendly: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Indicates whether this content is family friendly.",
    )
    editor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Specifies the Person who edited the CreativeWork.",
    )
    datePublished: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="Date of first broadcast/publication.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    assesses: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",
    )
    mainEntity: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="Indicates the primary entity described in some page or other CreativeWork.",
    )
    correction: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'CorrectionComment']], AnyUrl, 'URL', str, 'Text', 'CorrectionComment']] = Field(
        None,
        description="Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]],"
     "textually or in another document.",
    )
    timeRequired: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="Approximate or typical time it takes to work with or through this learning resource for"
     "the typical intended target audience, e.g. 'PT30M', 'PT1H25M'.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="Keywords or tags used to describe this content. Multiple entries in a keywords list are"
     "typically delimited by commas.",
    )
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    sponsor: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    educationalUse: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",
    )
    sdDatePublished: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="Indicates the date on which the current structured data was generated / published. Typically"
     "used alongside [[sdPublisher]]",
    )
    spatialCoverage: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of"
     "the content. It is a subproperty of contentLocation intended primarily for more technical"
     "and detailed materials. For example with a Dataset, it indicates areas that the dataset"
     "describes: a dataset of New York weather would have spatialCoverage which was the place:"
     "the state of New York.",
    )
    material: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Product']], AnyUrl, 'URL', str, 'Text', 'Product']] = Field(
        None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    publication: Optional[Union[List[Union['PublicationEvent', str]], 'PublicationEvent', str]] = Field(
        None,
        description="A publication event associated with the item.",
    )
    encodingFormat: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)"
     "and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types))"
     "e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.)."
     "In cases where a [[CreativeWork]] has several media type representations, [[encoding]]"
     "can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]]"
     "information. Unregistered or niche encoding and file formats can be indicated instead"
     "via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    dateModified: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date on which the CreativeWork was most recently modified or when the item's entry"
     "was modified within a DataFeed.",
    )
    reviews: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="Review of the item.",
    )
    dateCreated: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date on which the CreativeWork was created or the item was added to a DataFeed.",
    )
    associatedMedia: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    interpretedAsClaim: Optional[Union[List[Union['Claim', str]], 'Claim', str]] = Field(
        None,
        description="Used to indicate a specific claim contained, implied, translated or refined from the"
     "content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can"
     "be indicated using [[claimInterpreter]].",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="A review of the item.",
    )
    publisherImprint: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The publishing division which published the comic.",
    )
    accessibilityAPI: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Indicates that the resource is compatible with the referenced accessibility API ([WebSchemas"
     "wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    version: Optional[Union[List[Union[Decimal, 'Number', str, 'Text']], Decimal, 'Number', str, 'Text']] = Field(
        None,
        description="The version of the CreativeWork embodied by a specified resource.",
    )
    learningResourceType: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",
    )
    discussionUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        None,
        description="A link to the page containing the comments of the CreativeWork.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    fileFormat: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml))"
     "of the content e.g. application/zip of a SoftwareApplication binary. In cases where"
     "a CreativeWork has several media type representations, 'encoding' can be used to indicate"
     "each MediaObject alongside particular fileFormat information. Unregistered or niche"
     "file formats can be indicated instead via the most appropriate URL, e.g. defining Web"
     "page or a Wikipedia entry.",
    )
    producer: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="The person or organization who produced the work (e.g. music album, movie, tv/radio"
     "series etc.).",
    )
    citation: Optional[Union[List[Union[str, 'Text', 'CreativeWork']], str, 'Text', 'CreativeWork']] = Field(
        None,
        description="A citation or reference to another creative work, such as another publication, web page,"
     "scholarly article, etc.",
    )
    archivedAt: Optional[Union[List[Union[AnyUrl, 'URL', 'WebPage', str]], AnyUrl, 'URL', 'WebPage', str]] = Field(
        None,
        description="Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case"
     "of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible,"
     "but be archived by archival, journalistic, activist, or law enforcement organizations."
     "In such cases, the referenced page may not directly publish the content.",
    )
    encoding: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        None,
        description="A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.",
    )
    interactivityType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The predominant mode of learning supported by the learning resource. Acceptable values"
     "are 'active', 'expositive', or 'mixed'.",
    )
    spatial: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="The \"spatial\" property can be used in cases when more specific properties (e.g. [[locationCreated]],"
     "[[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.",
    )
    contentLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="The location depicted or described in the content. For example, the location in a photograph"
     "or painting.",
    )
    copyrightHolder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The party holding the legal copyright to the CreativeWork.",
    )
    contributor: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A secondary contributor to the CreativeWork or Event.",
    )
    isAccessibleForFree: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    accessibilityControl: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Identifies input methods that are sufficient to fully control the described resource"
     "([WebSchemas wiki lists possible values](http://www.w3.org/wiki/WebSchemas/Accessibility)).",
    )
    commentCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of comments this CreativeWork (e.g. Article, Question or Answer) has received."
     "This is most applicable to works published in Web sites with commenting system; additional"
     "comments may exist elsewhere.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.Comment import Comment
    from pydantic_schemaorg.AudioObject import AudioObject
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.Clip import Clip
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.PublicationEvent import PublicationEvent
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.SizeSpecification import SizeSpecification
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.Rating import Rating
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.CorrectionComment import CorrectionComment
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Claim import Claim
    from pydantic_schemaorg.WebPage import WebPage
