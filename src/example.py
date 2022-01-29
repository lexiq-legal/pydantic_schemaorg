from pydantic_schemaorg.ScholarlyArticle import ScholarlyArticle


scholarly_article = ScholarlyArticle(
    url="https://github.com/lexiq-legal/pydantic_schemaorg",
    sameAs="https://github.com/lexiq-legal/pydantic_schemaorg",
    copyrightNotice="Free to use under the MIT license",
    dateCreated="2021-11",
)
print(scholarly_article.json())
