from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import MyModel


@registry.register_document
class MyModelDocument(Document):

    class Index:
        name = 'mymodel'

    class Django:
        model = MyModel
        fields = ['name','email','message','created_at',]