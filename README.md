# pydantic_schemaorg

Use [Schema.org](https://schema.org) types in [pydantic](https://pydantic-docs.helpmanual.io/)! <br> <br>
**Pydantic_schemaorg** contains all the models defined by schema.org. The pydantic classes are auto-generated from the
schema.org model definitions that can be found
on [https://schema.org/version/latest/schemaorg-current-https.jsonld](https://schema.org/version/latest/schemaorg-current-https.jsonld)

## Requirements

Works with python >= 3.8

## How to install

```pip install pydantic-schemaorg```<br><br>
Import any class you want to use by with the following convention<br>
```from pydantic_schemaorg.<SCHEMAORG_MODEL_NAME> import <SCHEMAORG_MODEL_NAME>```<br><br>

A full (hierarchical) list of Schema.org model names can be found [here](https://schema.org/docs/full.html)

## Example usages

```
from pydantic_schemaorg.ScholarlyArticle import ScholarlyArticle

scholarly_article = ScholarlyArticle(url='https://github.com/lexiq-legal/pydantic_schemaorg',
                                    sameAs='https://github.com/lexiq-legal/pydantic_schemaorg',
                                    copyrightNotice='Free to use under the MIT license',
                                    dateCreated='15-12-2021')
print(scholarly_article.json())
```

```
{"@type": "ScholarlyArticle", "url": "https://github.com/lexiq-legal/pydantic_schemaorg", "sameAs": "https://github.com/lexiq-legal/pydantic_schemaorg", "copyrightNotice": "Free to use under the MIT license", "dateCreated": "15-12-2021"}
```