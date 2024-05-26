from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

description = """
Data Descript API helps you perform various statistical analyses on your data sets. 🚀

## Endpoints

### Descriptive Statistics

Calculate basic descriptive statistics for your data:
* **Mean**
* **Median**
* **Variance**
* **Standard Deviation**
* **Minimum and Maximum values**
* **Range**
* **Quartiles (Q1, Q2, Q3)**
"""

app = FastAPI(
    title="Data Descript API",
    description=description,
    version="0.0.1"
)


def custom_openapi():
    if not app.openapi_schema:
        app.openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            terms_of_service=app.terms_of_service,
            contact=app.contact,
            license_info=app.license_info,
            routes=app.routes,
            tags=app.openapi_tags,
            servers=app.servers,
        )
        for _, method_item in app.openapi_schema.get('paths').items():
            for _, param in method_item.items():
                responses = param.get('responses')
                # remove 422 response, also can remove other status code
                if '422' in responses:
                    responses['400'] = {'description': 'Bad Request', 'content': {
                        'application/json': {'schema': {'$ref': '#/components/schemas/HTTPValidationError'}}}}
                    del (responses['422'])
    return app.openapi_schema


app.openapi = custom_openapi
