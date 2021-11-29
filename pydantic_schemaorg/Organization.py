from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from datetime import date
from pydantic_schemaorg.Thing import Thing


class Organization(Thing):
    """An organization such as a school, NGO, corporation, club, etc.

    See https://schema.org/Organization.

    """

    subOrganization: Any = Field(
        None,
        description="A relationship between two organizations where the first includes the second, e.g.,"
     "as a subsidiary. See also: the more specific 'department' property.",
    )
    contactPoint: Any = Field(
        None,
        description="A contact point for a person or organization.",
    )
    areaServed: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    actionableFeedbackPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",
    )
    parentOrganization: Any = Field(
        None,
        description="The larger organization that this organization is a [[subOrganization]] of, if any.",
    )
    funder: Any = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    globalLocationNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    employees: Any = Field(
        None,
        description="People working for this organization.",
    )
    diversityPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",
    )
    aggregateRating: Any = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    knowsLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    award: Optional[Union[List[str], str]] = Field(
        None,
        description="An award won by or for this item.",
    )
    foundingLocation: Any = Field(
        None,
        description="The place where the Organization was founded.",
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
    isicV4: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    member: Any = Field(
        None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",
    )
    naics: Optional[Union[List[str], str]] = Field(
        None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    employee: Any = Field(
        None,
        description="Someone working for this organization.",
    )
    brand: Any = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    duns: Optional[Union[List[str], str]] = Field(
        None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    hasMerchantReturnPolicy: Any = Field(
        None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    location: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    interactionStatistic: Any = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    hasCredential: Any = Field(
        None,
        description="A credential awarded to the Person or Organization.",
    )
    nonprofitStatus: Any = Field(
        None,
        description="nonprofit Status indicates the legal status of a non-profit organization in its primary"
     "place of business.",
    )
    ethicsPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",
    )
    correctionsPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",
    )
    memberOf: Any = Field(
        None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    slogan: Optional[Union[List[str], str]] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    department: Any = Field(
        None,
        description="A relationship between an organization and a department of that organization, also"
     "described as an organization (allowing different urls, logos, opening hours). For"
     "example: a store with a pharmacy, or a bakery with a cafe.",
    )
    vatID: Optional[Union[List[str], str]] = Field(
        None,
        description="The Value-added Tax ID of the organization or person.",
    )
    leiCode: Optional[Union[List[str], str]] = Field(
        None,
        description="An organization identifier that uniquely identifies a legal entity as defined in ISO"
     "17442.",
    )
    founders: Any = Field(
        None,
        description="A person who founded this organization.",
    )
    logo: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="An associated logo.",
    )
    members: Any = Field(
        None,
        description="A member of this organization.",
    )
    foundingDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date that this organization was founded.",
    )
    awards: Optional[Union[List[str], str]] = Field(
        None,
        description="Awards won by or for this item.",
    )
    makesOffer: Any = Field(
        None,
        description="A pointer to products or services offered by the organization or person.",
    )
    address: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Physical address of the item.",
    )
    dissolutionDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date that this organization was dissolved.",
    )
    alumni: Any = Field(
        None,
        description="Alumni of an organization.",
    )
    sponsor: Any = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    events: Any = Field(
        None,
        description="Upcoming or past events associated with this place or organization.",
    )
    serviceArea: Any = Field(
        None,
        description="The geographic area where the service is provided.",
    )
    email: Optional[Union[List[str], str]] = Field(
        None,
        description="Email address.",
    )
    taxID: Optional[Union[List[str], str]] = Field(
        None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    hasOfferCatalog: Any = Field(
        None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    numberOfEmployees: Any = Field(
        None,
        description="The number of employees in an organization e.g. business.",
    )
    ownershipFundingInfo: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",
    )
    founder: Any = Field(
        None,
        description="A person who founded this organization.",
    )
    reviews: Any = Field(
        None,
        description="Review of the item.",
    )
    telephone: Optional[Union[List[str], str]] = Field(
        None,
        description="The telephone number.",
    )
    hasPOS: Any = Field(
        None,
        description="Points-of-Sales operated by the organization or person.",
    )
    review: Any = Field(
        None,
        description="A review of the item.",
    )
    seeks: Any = Field(
        None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    contactPoints: Any = Field(
        None,
        description="A contact point for a person or organization.",
    )
    legalName: Optional[Union[List[str], str]] = Field(
        None,
        description="The official name of the organization, e.g. the registered company name.",
    )
    diversityStaffingReport: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",
    )
    unnamedSourcesPolicy: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",
    )
    knowsAbout: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    event: Any = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    faxNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The fax number.",
    )
    owns: Any = Field(
        None,
        description="Products owned by the organization or person.",
    )
    locals().update({"@type": Field("Organization", const=True)})


Organization.update_forward_refs()
