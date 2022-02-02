from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.EducationalOccupationalProgram import EducationalOccupationalProgram


class WorkBasedProgram(EducationalOccupationalProgram):
    """A program with both an educational and employment component. Typically based at a workplace"
     "and structured around work-based learning, with the aim of instilling competencies"
     "related to an occupation. WorkBasedProgram is used to distinguish programs such as"
     "apprenticeships from school, college or other classroom based educational programs.

    See: https://schema.org/WorkBasedProgram
    Model depth: 4
    """
    type_: str = Field("WorkBasedProgram", alias='@type')
    trainingSalary: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        None,
        description="The estimated salary earned while in the program.",
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
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CategoryCode import CategoryCode
