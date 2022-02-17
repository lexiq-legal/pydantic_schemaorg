from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Person(Thing):
    """A person (alive, dead, undead, or fictional).

    See: https://schema.org/Person
    Model depth: 2
    """
    type_: str = Field(default="Person", alias='@type')
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    colleagues: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A colleague of the person.",
    )
    jobTitle: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The job title of the person (for example, Financial Manager).",
    )
    nationality: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        default=None,
        description="Nationality of the person.",
    )
    honorificPrefix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.",
    )
    workLocation: Optional[Union[List[Union['ContactPoint', 'Place', str]], 'ContactPoint', 'Place', str]] = Field(
        default=None,
        description="A contact location for a person's place of work.",
    )
    alumniOf: Optional[Union[List[Union['EducationalOrganization', 'Organization', str]], 'EducationalOrganization', 'Organization', str]] = Field(
        default=None,
        description="An organization that the person is an alumni of.",
    )
    funder: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    knowsLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    netWorth: Optional[Union[List[Union['PriceSpecification', 'MonetaryAmount', str]], 'PriceSpecification', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The total financial value of the person as calculated by subtracting assets from liabilities.",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    relatedTo: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic familial relation.",
    )
    honorificSuffix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An honorific suffix following a Person's name such as M.D. /PhD/MSCSW.",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual e.g. a [[Person]] writing"
     "a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies."
     "When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those"
     "of the party primarily responsible for the creation of the [[CreativeWork]]. While"
     "such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    isicV4: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    birthPlace: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The place where the person was born.",
    )
    parent: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A parent of this person.",
    )
    gender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        default=None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who do not identify as a binary gender."
     "The [[gender]] property can also be used in an extended sense to cover e.g. the gender"
     "of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities."
     "A mixed-gender [[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    familyName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Family name. In the U.S., the last name of a Person.",
    )
    naics: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    sibling: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sibling of the person.",
    )
    siblings: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sibling of the person.",
    )
    brand: Optional[Union[List[Union['Brand', 'Organization', str]], 'Brand', 'Organization', str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    duns: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    interactionStatistic: Optional[Union[List[Union['InteractionCounter', str]], 'InteractionCounter', str]] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    hasCredential: Optional[Union[List[Union['EducationalOccupationalCredential', str]], 'EducationalOccupationalCredential', str]] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",
    )
    memberOf: Optional[Union[List[Union['Organization', 'ProgramMembership', str]], 'Organization', 'ProgramMembership', str]] = Field(
        default=None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    givenName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Given name. In the U.S., the first name of a Person.",
    )
    height: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    vatID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Value-added Tax ID of the organization or person.",
    )
    affiliation: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="An organization that this person is affiliated with. For example, a school/university,"
     "a club, or a team.",
    )
    children: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A child of the person.",
    )
    spouse: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The person's spouse.",
    )
    additionalName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An additional name for a Person, can be used for a middle name.",
    )
    follows: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic uni-directional social relation.",
    )
    deathDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        default=None,
        description="Date of death.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Awards won by or for this item.",
    )
    makesOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        default=None,
        description="Physical address of the item.",
    )
    birthDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        default=None,
        description="Date of birth.",
    )
    sponsor: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    deathPlace: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The place where the person died.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Email address.",
    )
    taxID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    hasOccupation: Optional[Union[List[Union['Occupation', str]], 'Occupation', str]] = Field(
        default=None,
        description="The Person's occupation. For past professions, use Role for expressing dates.",
    )
    hasOfferCatalog: Optional[Union[List[Union['OfferCatalog', str]], 'OfferCatalog', str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    knows: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic bi-directional social/work relation.",
    )
    worksFor: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="Organizations that the person works for.",
    )
    telephone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The telephone number.",
    )
    hasPOS: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Points-of-Sales operated by the organization or person.",
    )
    colleague: Optional[Union[List[Union[AnyUrl, 'URL', 'Person', str]], AnyUrl, 'URL', 'Person', str]] = Field(
        default=None,
        description="A colleague of the person.",
    )
    performerIn: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Event that this person is a performer or participant in.",
    )
    seeks: Optional[Union[List[Union['Demand', str]], 'Demand', str]] = Field(
        default=None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    contactPoints: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    homeLocation: Optional[Union[List[Union['ContactPoint', 'Place', str]], 'ContactPoint', 'Place', str]] = Field(
        default=None,
        description="A contact location for a person's residence.",
    )
    callSign: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    parents: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A parents of the person.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The fax number.",
    )
    owns: Optional[Union[List[Union['Product', 'OwnershipInfo', str]], 'Product', 'OwnershipInfo', str]] = Field(
        default=None,
        description="Products owned by the organization or person.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.EducationalOrganization import EducationalOrganization
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.ProgramMembership import ProgramMembership
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Occupation import Occupation
    from pydantic_schemaorg.OfferCatalog import OfferCatalog
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
