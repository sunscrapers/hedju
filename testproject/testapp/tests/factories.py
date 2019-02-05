from factory.django import DjangoModelFactory


class ExampleFactory(DjangoModelFactory):
    class Meta:
        model = 'testapp.Example'
