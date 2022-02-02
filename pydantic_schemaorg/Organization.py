from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Organization(Thing):
    """An organization such as a school, NGO, corporation, club, etc.

    See: https://schema.org/Organization
    Model depth: 2
    """
    type_: str = Field("Organization", alias='@type')
    subOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="A relationship between two organizations where the first includes the second, e.g.,"
     "as a subsidiary. See also: the more specific 'department' property.",
    )
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        None,
        description="A contact point for a person or organization.",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']], str, 'Text', 'GeoShape', 'Place', 'AdministrativeArea']] = Field(
        None,
        description="The geographic area where a service or offered item is provided.",
    )
    actionableFeedbackPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",
    )
    parentOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="The larger organization that this organization is a [[subOrganization]] of, if any.",
    )
    funder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    employees: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="People working for this organization.",
    )
    diversityPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
    )
    knowsLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An award won by or for this item.",
    )
    foundingLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="The place where the Organization was founded.",
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
    isicV4: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    member: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",
    )
    naics: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    employee: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Someone working for this organization.",
    )
    brand: Optional[Union[List[Union['Organization', 'Brand', str]], 'Organization', 'Brand', str]] = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    duns: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[Union['MerchantReturnPolicy', str]], 'MerchantReturnPolicy', str]] = Field(
        None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    location: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']], str, 'Text', 'PostalAddress', 'Place', 'VirtualLocation']] = Field(
        None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
    )
    interactionStatistic: Optional[Union[List[Union['InteractionCounter', str]], 'InteractionCounter', str]] = Field(
        None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    hasCredential: Optional[Union[List[Union['EducationalOccupationalCredential', str]], 'EducationalOccupationalCredential', str]] = Field(
        None,
        description="A credential awarded to the Person or Organization.",
    )
    nonprofitStatus: Optional[Union[List[Union['NonprofitType', str]], 'NonprofitType', str]] = Field(
        None,
        description="nonprofit Status indicates the legal status of a non-profit organization in its primary"
     "place of business.",
    )
    ethicsPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",
    )
    correctionsPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",
    )
    memberOf: Optional[Union[List[Union['ProgramMembership', 'Organization', str]], 'ProgramMembership', 'Organization', str]] = Field(
        None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A slogan or motto associated with the item.",
    )
    department: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        None,
        description="A relationship between an organization and a department of that organization, also"
     "described as an organization (allowing different urls, logos, opening hours). For"
     "example: a store with a pharmacy, or a bakery with a cafe.",
    )
    vatID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The Value-added Tax ID of the organization or person.",
    )
    leiCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="An organization identifier that uniquely identifies a legal entity as defined in ISO"
     "17442.",
    )
    founders: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A person who founded this organization.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        None,
        description="An associated logo.",
    )
    members: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        None,
        description="A member of this organization.",
    )
    foundingDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date that this organization was founded.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Awards won by or for this item.",
    )
    makesOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        None,
        description="A pointer to products or services offered by the organization or person.",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        None,
        description="Physical address of the item.",
    )
    dissolutionDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date that this organization was dissolved.",
    )
    alumni: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="Alumni of an organization.",
    )
    sponsor: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    events: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="Upcoming or past events associated with this place or organization.",
    )
    serviceArea: Optional[Union[List[Union['GeoShape', 'Place', 'AdministrativeArea', str]], 'GeoShape', 'Place', 'AdministrativeArea', str]] = Field(
        None,
        description="The geographic area where the service is provided.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Email address.",
    )
    taxID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    hasOfferCatalog: Optional[Union[List[Union['OfferCatalog', str]], 'OfferCatalog', str]] = Field(
        None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    numberOfEmployees: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        None,
        description="The number of employees in an organization e.g. business.",
    )
    ownershipFundingInfo: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'AboutPage', 'CreativeWork']], AnyUrl, 'URL', str, 'Text', 'AboutPage', 'CreativeWork']] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",
    )
    founder: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A person who founded this organization.",
    )
    reviews: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="Review of the item.",
    )
    telephone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The telephone number.",
    )
    hasPOS: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        None,
        description="Points-of-Sales operated by the organization or person.",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="A review of the item.",
    )
    seeks: Optional[Union[List[Union['Demand', str]], 'Demand', str]] = Field(
        None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    contactPoints: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        None,
        description="A contact point for a person or organization.",
    )
    legalName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The official name of the organization, e.g. the registered company name.",
    )
    diversityStaffingReport: Optional[Union[List[Union[AnyUrl, 'URL', 'Article', str]], AnyUrl, 'URL', 'Article', str]] = Field(
        None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",
    )
    unnamedSourcesPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The fax number.",
    )
    owns: Optional[Union[List[Union['OwnershipInfo', 'Product', str]], 'OwnershipInfo', 'Product', str]] = Field(
        None,
        description="Products owned by the organization or person.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.NonprofitType import NonprofitType
    from pydantic_schemaorg.ProgramMembership import ProgramMembership
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.AboutPage import AboutPage
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Article import Article
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
    from pydantic_schemaorg.Product import Product
