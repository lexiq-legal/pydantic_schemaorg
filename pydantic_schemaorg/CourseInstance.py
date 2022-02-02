from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Event import Event


class CourseInstance(Event):
    """An instance of a [[Course]] which is distinct from other instances because it is offered"
     "at a different time or location or through different media or modes of study or to a specific"
     "section of students.

    See: https://schema.org/CourseInstance
    Model depth: 3
    """
    type_: str = Field("CourseInstance", alias='@type')
    courseWorkload: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The amount of work expected of students taking the course, often provided as a figure"
     "per week or per month, and may be broken down by type. For example, \"2 hours of lectures,"
     "1 hour of lab work and 3 hours of independent study per week\".",
    )
    instructor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A person assigned to instruct or provide instructional assistance for the [[CourseInstance]].",
    )
    courseMode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        None,
        description="The medium or means of delivery of the course instance or the mode of study, either as a"
     "text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\" or \"asynchronous\";"
     "\"full-time\" or \"part-time\") or as a URL reference to a term from a controlled vocabulary"
     "(e.g. https://ceds.ed.gov/element/001311#Asynchronous ).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.URL import URL
