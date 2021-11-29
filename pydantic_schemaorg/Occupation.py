from pydantic import Field
from pydantic_schemaorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTerm import DefinedTerm
from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
from decimal import Decimal
from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.Intangible import Intangible


class Occupation(Intangible):
    """A profession, may involve prolonged training and/or a formal qualification.

    See https://schema.org/Occupation.

    """

    experienceRequirements: Optional[Union[List[Union[str, OccupationalExperienceRequirements]], Union[str, OccupationalExperienceRequirements]]] = Field(
        None,
        description="Description of skills and experience needed for the position or Occupation.",
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
    occupationLocation: Optional[Union[List[AdministrativeArea], AdministrativeArea]] = Field(
        None,
        description="The region/country for which this occupational description is appropriate. Note that"
     "educational requirements and qualifications can vary between jurisdictions.",
    )
    responsibilities: Optional[Union[List[str], str]] = Field(
        None,
        description="Responsibilities associated with this role or Occupation.",
    )
    qualifications: Optional[Union[List[Union[str, EducationalOccupationalCredential]], Union[str, EducationalOccupationalCredential]]] = Field(
        None,
        description="Specific qualifications required for this role or Occupation.",
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
    educationRequirements: Optional[Union[List[Union[str, EducationalOccupationalCredential]], Union[str, EducationalOccupationalCredential]]] = Field(
        None,
        description="Educational background needed for the position or Occupation.",
    )
    locals().update({"@type": Field("Occupation", const=True)})


Occupation.update_forward_refs()
