from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import AnyUrl
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve"
     "an outcome, usually a credential like a degree or certificate. This would define a discrete"
     "set of opportunities (e.g., job, courses) that together constitute a program with a"
     "clear start, end, set of requirements, and transition to a new occupational opportunity"
     "(e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    See: https://schema.org/EducationalOccupationalProgram
    Model depth: 3
    """
    type_: str = Field("EducationalOccupationalProgram", alias='@type')
    timeToComplete: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The expected length of time to complete the program if attending full-time.",
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
    typicalCreditsPerTerm: Optional[Union[List[Union[int, 'Integer', 'StructuredValue', str]], int, 'Integer', 'StructuredValue', str]] = Field(
        None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however"
     "'term' is defined by the institution.",
    )
    applicationStartDate: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date at which the program begins collecting applications for the next enrollment"
     "cycle.",
    )
    programPrerequisites: Optional[Union[List[Union[str, 'Text', 'Course', 'EducationalOccupationalCredential', 'AlignmentObject']], str, 'Text', 'Course', 'EducationalOccupationalCredential', 'AlignmentObject']] = Field(
        None,
        description="Prerequisites for enrolling in the program.",
    )
    numberOfCredits: Optional[Union[List[Union[int, 'Integer', 'StructuredValue', str]], int, 'Integer', 'StructuredValue', str]] = Field(
        None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    educationalProgramMode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="Similar to courseMode, The medium or means of delivery of the program as a whole. The value"
     "may either be a text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\""
     "or \"asynchronous\"; \"full-time\" or \"part-time\") or a URL reference to a term from"
     "a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous"
     ").",
    )
    programType: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="The type of educational or occupational program. For example, classroom, internship,"
     "alternance, etc..",
    )
    applicationDeadline: Optional[Union[List[Union[ISO8601Date, 'Date', str]], ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date at which the program stops collecting applications for the next enrollment"
     "cycle.",
    )
    educationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    maximumEnrollment: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The maximum number of students who may be enrolled in the program.",
    )
    termDuration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The amount of time in a term as defined by the institution. A term is a length of time where"
     "students take one or more classes. Semesters and quarters are common units for term.",
    )
    endDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    trainingSalary: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        None,
        description="The estimated salary earned while in the program.",
    )
    salaryUponCompletion: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        None,
        description="The expected salary upon completing the training.",
    )
    timeOfDay: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The time of day the program normally runs. For example, \"evenings\".",
    )
    termsPerYear: Optional[Union[List[Union[Decimal, 'Number', str]], Decimal, 'Number', str]] = Field(
        None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common"
     "units for term. For example, if the student can only take 2 semesters for the program in"
     "one year, then termsPerYear should be 2.",
    )
    occupationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    startDate: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    dayOfWeek: Optional[Union[List[Union['DayOfWeek', str]], 'DayOfWeek', str]] = Field(
        None,
        description="The day of the week for which these opening hours are valid.",
    )
    financialAidEligible: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    occupationalCategory: Optional[Union[List[Union[str, 'Text', 'CategoryCode']], str, 'Text', 'CategoryCode']] = Field(
        None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    hasCourse: Optional[Union[List[Union['Course', str]], 'Course', str]] = Field(
        None,
        description="A course or class that is one of the learning opportunities that constitute an educational"
     "/ occupational program. No information is implied about whether the course is mandatory"
     "or optional; no guarantee is implied about whether the course will be available to everyone"
     "on the program.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Course import Course
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.CategoryCode import CategoryCode
