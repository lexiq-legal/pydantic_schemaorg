from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Place import Place
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.CreativeWork import CreativeWork
from datetime import date
from pydantic_schemaorg.Thing import Thing


class Person(Thing):
    """A person (alive, dead, undead, or fictional).

    See https://schema.org/Person.

    """

    contactPoint: Any = Field(
        None,
        description="A contact point for a person or organization.",
    )
    colleagues: Any = Field(
        None,
        description="A colleague of the person.",
    )
    jobTitle: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The job title of the person (for example, Financial Manager).",
    )
    nationality: Any = Field(
        None,
        description="Nationality of the person.",
    )
    honorificPrefix: Optional[Union[List[str], str]] = Field(
        None,
        description="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.",
    )
    workLocation: Union[List[Union[Place, Any]], Union[Place, Any]] = Field(
        None,
        description="A contact location for a person's place of work.",
    )
    alumniOf: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="An organization that the person is an alumni of.",
    )
    funder: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
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
    weight: Any = Field(
        None,
        description="The weight of the product or person.",
    )
    knowsLanguage: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    netWorth: Any = Field(
        None,
        description="The total financial value of the person as calculated by subtracting assets from liabilities.",
    )
    award: Optional[Union[List[str], str]] = Field(
        None,
        description="An award won by or for this item.",
    )
    relatedTo: Any = Field(
        None,
        description="The most generic familial relation.",
    )
    honorificSuffix: Optional[Union[List[str], str]] = Field(
        None,
        description="An honorific suffix following a Person's name such as M.D. /PhD/MSCSW.",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, CreativeWork]], Union[AnyUrl, CreativeWork]]] = Field(
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
    birthPlace: Optional[Union[List[Place], Place]] = Field(
        None,
        description="The place where the person was born.",
    )
    parent: Any = Field(
        None,
        description="A parent of this person.",
    )
    gender: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who do not identify as a binary gender."
     "The [[gender]] property can also be used in an extended sense to cover e.g. the gender"
     "of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities."
     "A mixed-gender [[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    familyName: Optional[Union[List[str], str]] = Field(
        None,
        description="Family name. In the U.S., the last name of a Person.",
    )
    naics: Optional[Union[List[str], str]] = Field(
        None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    sibling: Any = Field(
        None,
        description="A sibling of the person.",
    )
    siblings: Any = Field(
        None,
        description="A sibling of the person.",
    )
    brand: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    duns: Optional[Union[List[str], str]] = Field(
        None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
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
    memberOf: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    givenName: Optional[Union[List[str], str]] = Field(
        None,
        description="Given name. In the U.S., the first name of a Person.",
    )
    height: Any = Field(
        None,
        description="The height of the item.",
    )
    vatID: Optional[Union[List[str], str]] = Field(
        None,
        description="The Value-added Tax ID of the organization or person.",
    )
    affiliation: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="An organization that this person is affiliated with. For example, a school/university,"
     "a club, or a team.",
    )
    children: Any = Field(
        None,
        description="A child of the person.",
    )
    spouse: Any = Field(
        None,
        description="The person's spouse.",
    )
    additionalName: Optional[Union[List[str], str]] = Field(
        None,
        description="An additional name for a Person, can be used for a middle name.",
    )
    follows: Any = Field(
        None,
        description="The most generic uni-directional social relation.",
    )
    deathDate: Optional[Union[List[date], date]] = Field(
        None,
        description="Date of death.",
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
    birthDate: Optional[Union[List[date], date]] = Field(
        None,
        description="Date of birth.",
    )
    sponsor: Union[List[Union[Organization, Any]], Union[Organization, Any]] = Field(
        None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    deathPlace: Optional[Union[List[Place], Place]] = Field(
        None,
        description="The place where the person died.",
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
    hasOccupation: Any = Field(
        None,
        description="The Person's occupation. For past professions, use Role for expressing dates.",
    )
    hasOfferCatalog: Any = Field(
        None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    knows: Any = Field(
        None,
        description="The most generic bi-directional social/work relation.",
    )
    worksFor: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="Organizations that the person works for.",
    )
    telephone: Optional[Union[List[str], str]] = Field(
        None,
        description="The telephone number.",
    )
    hasPOS: Optional[Union[List[Place], Place]] = Field(
        None,
        description="Points-of-Sales operated by the organization or person.",
    )
    colleague: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A colleague of the person.",
    )
    performerIn: Any = Field(
        None,
        description="Event that this person is a performer or participant in.",
    )
    seeks: Any = Field(
        None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    contactPoints: Any = Field(
        None,
        description="A contact point for a person or organization.",
    )
    homeLocation: Union[List[Union[Place, Any]], Union[Place, Any]] = Field(
        None,
        description="A contact location for a person's residence.",
    )
    callSign: Optional[Union[List[str], str]] = Field(
        None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    parents: Any = Field(
        None,
        description="A parents of the person.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, str, Thing]], Union[AnyUrl, str, Thing]]] = Field(
        None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    faxNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The fax number.",
    )
    owns: Any = Field(
        None,
        description="Products owned by the organization or person.",
    )
    locals().update({"@type": Field("Person", const=True)})


Person.update_forward_refs()
