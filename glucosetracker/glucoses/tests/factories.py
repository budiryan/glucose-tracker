from datetime import datetime, date, timedelta

from factory import DjangoModelFactory, Sequence, SubFactory
from factory.fuzzy import FuzzyInteger, FuzzyNaiveDateTime

from accounts.tests.factories import UserFactory

from ..models import Glucose, Category, Color


class CategoryFactory(DjangoModelFactory):
    FACTORY_FOR = Category

    name = Sequence(lambda n: 'Category{0}'.format(n))


class GlucoseFactory(DjangoModelFactory):
    FACTORY_FOR = Glucose

    user = SubFactory(UserFactory)
    value = FuzzyInteger(0, 50)
    category = SubFactory(CategoryFactory)
    record_date = date.today()
    record_time = FuzzyNaiveDateTime(datetime.now() - timedelta(hours=24))
    notes = 'This is a randomly generated dummy urine glucose data'


class ColorFactory(DjangoModelFactory):
    FACTORY_FOR = Color
    user = SubFactory(UserFactory)
    value = FuzzyInteger(0, 8)
    category = SubFactory(CategoryFactory)
    record_date = date.today()
    record_time = FuzzyNaiveDateTime(datetime.now() - timedelta(hours=24))
    notes = 'This is a randomly generated dummy urine color data'
