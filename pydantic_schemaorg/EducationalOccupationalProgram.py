from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Demand import Demand
from pydantic_schemaorg.StructuredValue import StructuredValue
from datetime import date, datetime
from pydantic_schemaorg.AlignmentObject import AlignmentObject
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from decimal import Decimal
from pydantic_schemaorg.DayOfWeek import DayOfWeek
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Intangible import Intangible


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve"
     "an outcome, usually a credential like a degree or certificate. This would define a discrete"
     "set of opportunities (e.g., job, courses) that together constitute a program with a"
     "clear start, end, set of requirements, and transition to a new occupational opportunity"
     "(e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    See https://schema.org/EducationalOccupationalProgram.

    """

    timeToComplete: Any = Field(
        None,
        description="The expected length of time to complete the program if attending full-time.",
    )
    offers: Union[List[Union[Demand, Any]], Union[Demand, Any]] = Field(
        None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    typicalCreditsPerTerm: Optional[Union[List[Union[int, StructuredValue]], Union[int, StructuredValue]]] = Field(
        None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however"
     "'term' is defined by the institution.",
    )
    applicationStartDate: Optional[Union[List[date], date]] = Field(
        None,
        description="The date at which the program begins collecting applications for the next enrollment"
     "cycle.",
    )
    programPrerequisites: Union[List[Union[str, AlignmentObject, Any]], Union[str, AlignmentObject, Any]] = Field(
        None,
        description="Prerequisites for enrolling in the program.",
    )
    numberOfCredits: Optional[Union[List[Union[int, StructuredValue]], Union[int, StructuredValue]]] = Field(
        None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    educationalProgramMode: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="Similar to courseMode, The medium or means of delivery of the program as a whole. The value"
     "may either be a text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\""
     "or \"asynchronous\"; \"full-time\" or \"part-time\") or a URL reference to a term from"
     "a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous"
     ").",
    )
    programType: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The type of educational or occupational program. For example, classroom, internship,"
     "alternance, etc..",
    )
    applicationDeadline: Optional[Union[List[date], date]] = Field(
        None,
        description="The date at which the program stops collecting applications for the next enrollment"
     "cycle.",
    )
    educationalCredentialAwarded: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    maximumEnrollment: Optional[Union[List[int], int]] = Field(
        None,
        description="The maximum number of students who may be enrolled in the program.",
    )
    termDuration: Any = Field(
        None,
        description="The amount of time in a term as defined by the institution. A term is a length of time where"
     "students take one or more classes. Semesters and quarters are common units for term.",
    )
    endDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    trainingSalary: Any = Field(
        None,
        description="The estimated salary earned while in the program.",
    )
    salaryUponCompletion: Any = Field(
        None,
        description="The expected salary upon completing the training.",
    )
    timeOfDay: Optional[Union[List[str], str]] = Field(
        None,
        description="The time of day the program normally runs. For example, \"evenings\".",
    )
    termsPerYear: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common"
     "units for term. For example, if the student can only take 2 semesters for the program in"
     "one year, then termsPerYear should be 2.",
    )
    occupationalCredentialAwarded: Union[List[Union[AnyUrl, str, Any]], Union[AnyUrl, str, Any]] = Field(
        None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    startDate: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    dayOfWeek: Optional[Union[List[DayOfWeek], DayOfWeek]] = Field(
        None,
        description="The day of the week for which these opening hours are valid.",
    )
    financialAidEligible: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",
    )
    provider: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    occupationalCategory: Optional[Union[List[Union[str, CategoryCode]], Union[str, CategoryCode]]] = Field(
        None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    hasCourse: Any = Field(
        None,
        description="A course or class that is one of the learning opportunities that constitute an educational"
     "/ occupational program. No information is implied about whether the course is mandatory"
     "or optional; no guarantee is implied about whether the course will be available to everyone"
     "on the program.",
    )
    locals().update({"@type": Field("EducationalOccupationalProgram", const=True)})


EducationalOccupationalProgram.update_forward_refs()
