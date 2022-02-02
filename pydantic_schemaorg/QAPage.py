from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class QAPage(WebPage):
    """A QAPage is a WebPage focussed on a specific Question and its Answer(s), e.g. in a question"
     "answering site or documenting Frequently Asked Questions (FAQs).

    See: https://schema.org/QAPage
    Model depth: 4
    """
    type_: str = Field("QAPage", alias='@type')
    

