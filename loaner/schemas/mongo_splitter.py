from pydantic import BaseModel

from pydantic import BaseModel

def serialize_document(document: dict, model: BaseModel) -> str:
    if '_id' in document:
        document['id'] = str(document['_id'])
        del document['_id']

    instance:BaseModel = model(**document)  
    return instance.model_dump_json()
