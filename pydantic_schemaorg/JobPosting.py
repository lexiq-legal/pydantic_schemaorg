from pydantic import Field, AnyUrl, StrictBool
from pydantic_schemaorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
from decimal import Decimal
from pydantic_schemaorg.Place import Place
from datetime import date, datetime
from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Intangible import Intangible


class JobPosting(Intangible):
    """A listing that describes a job opening in a certain organization.

    See https://schema.org/JobPosting.

    """

    experienceRequirements: Optional[Union[List[Union[str, OccupationalExperienceRequirements]], Union[str, OccupationalExperienceRequirements]]] = Field(
        None,
        description="Description of skills and experience needed for the position or Occupation.",
    )
    hiringOrganization: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="Organization offering the job position.",
    )
    directApply: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct"
     "application for the job, via the posting website. A job posting is considered to have"
     "directApply of [[True]] if an application process for the specified job can be directly"
     "initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless"
     "be involved at an implementation level). A value of [[False]] is appropriate if there"
     "is no clear path to applying directly online for the specified job, navigating directly"
     "from the JobPosting url(s) supplied.",
    )
    skills: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is desired or required to fulfill this role or to work in this occupation.",
    )
    estimatedSalary: Union[List[Union[Decimal, MonetaryAmountDistribution, Any]], Union[Decimal, MonetaryAmountDistribution, Any]] = Field(
        None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",
    )
    benefits: Optional[Union[List[str], str]] = Field(
        None,
        description="Description of benefits associated with the job.",
    )
    sensoryRequirement: Optional[Union[List[Union[AnyUrl, str, DefinedTerm]], Union[AnyUrl, str, DefinedTerm]]] = Field(
        None,
        description="A description of any sensory requirements and levels necessary to function on the job,"
     "including hearing and vision. Defined terms such as those in O*net may be used, but note"
     "that there is no way to specify the level of ability as well as its nature when using a defined"
     "term.",
    )
    jobImmediateStart: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="An indicator as to whether a position is available for an immediate start.",
    )
    physicalRequirement: Optional[Union[List[Union[AnyUrl, str, DefinedTerm]], Union[AnyUrl, str, DefinedTerm]]] = Field(
        None,
        description="A description of the types of physical activity associated with the job. Defined terms"
     "such as those in O*net may be used, but note that there is no way to specify the level of ability"
     "as well as its nature when using a defined term.",
    )
    jobLocation: Optional[Union[List[Place], Place]] = Field(
        None,
        description="A (typically single) geographic location associated with the job position.",
    )
    incentives: Optional[Union[List[str], str]] = Field(
        None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    employerOverview: Optional[Union[List[str], str]] = Field(
        None,
        description="A description of the employer, career opportunities and work environment for this position.",
    )
    specialCommitments: Optional[Union[List[str], str]] = Field(
        None,
        description="Any special commitments associated with this job posting. Valid entries include VeteranCommit,"
     "MilitarySpouseCommit, etc.",
    )
    jobLocationType: Optional[Union[List[str], str]] = Field(
        None,
        description="A description of the job location (e.g TELECOMMUTE for telecommute jobs).",
    )
    title: Optional[Union[List[str], str]] = Field(
        None,
        description="The title of the job.",
    )
    totalJobOpenings: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of positions open for this job posting. Use a positive integer. Do not use if"
     "the number of positions is unclear or not known.",
    )
    salaryCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) )"
     "used for the main salary information in this job posting or for this employee.",
    )
    responsibilities: Optional[Union[List[str], str]] = Field(
        None,
        description="Responsibilities associated with this role or Occupation.",
    )
    securityClearanceRequirement: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A description of any security clearance requirements of the job.",
    )
    datePosted: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="Publication date of an online listing.",
    )
    qualifications: Optional[Union[List[Union[str, EducationalOccupationalCredential]], Union[str, EducationalOccupationalCredential]]] = Field(
        None,
        description="Specific qualifications required for this role or Occupation.",
    )
    jobStartDate: Optional[Union[List[Union[date, str]], Union[date, str]]] = Field(
        None,
        description="The date on which a successful applicant for this job would be expected to start work."
     "Choose a specific date in the future or use the jobImmediateStart property to indicate"
     "the position is to be filled as soon as possible.",
    )
    incentiveCompensation: Optional[Union[List[str], str]] = Field(
        None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    industry: Optional[Union[List[Union[str, DefinedTerm]], Union[str, DefinedTerm]]] = Field(
        None,
        description="The industry associated with the job position.",
    )
    employmentUnit: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="Indicates the department, unit and/or facility where the employee reports and/or in"
     "which the job is to be performed.",
    )
    baseSalary: Union[List[Union[Decimal, PriceSpecification, Any]], Union[Decimal, PriceSpecification, Any]] = Field(
        None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    validThrough: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    workHours: Optional[Union[List[str], str]] = Field(
        None,
        description="The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).",
    )
    experienceInPlaceOfEducation: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]])"
     "in place of its formal educational qualifications (as indicated by [[educationRequirements]])."
     "If true, indicates that satisfying one of these requirements is sufficient.",
    )
    jobBenefits: Optional[Union[List[str], str]] = Field(
        None,
        description="Description of benefits associated with the job.",
    )
    applicantLocationRequirements: Optional[Union[List[AdministrativeArea], AdministrativeArea]] = Field(
        None,
        description="The location(s) applicants can apply from. This is usually used for telecommuting jobs"
     "where the applicant does not need to be in a physical office. Note: This should not be used"
     "for citizenship or work visa requirements.",
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
    employmentType: Optional[Union[List[str], str]] = Field(
        None,
        description="Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).",
    )
    educationRequirements: Optional[Union[List[Union[str, EducationalOccupationalCredential]], Union[str, EducationalOccupationalCredential]]] = Field(
        None,
        description="Educational background needed for the position or Occupation.",
    )
    applicationContact: Any = Field(
        None,
        description="Contact details for further information relevant to this job posting.",
    )
    relevantOccupation: Any = Field(
        None,
        description="The Occupation for the JobPosting.",
    )
    eligibilityToWorkRequirement: Optional[Union[List[str], str]] = Field(
        None,
        description="The legal requirements such as citizenship, visa and other documentation required"
     "for an applicant to this job.",
    )
    locals().update({"@type": Field("JobPosting", const=True)})


JobPosting.update_forward_refs()
