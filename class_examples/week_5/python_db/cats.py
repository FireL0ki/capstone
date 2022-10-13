from peewee import *

db = SqliteDatabase('cats.sqlite')

class Owner(Model):
    name = CharField()

    class Meta: 
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}'

class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    owner = ForeignKeyField(Owner, backref='cats') # set up foreign key to connect cat table & owner table

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}, Owner: {self.owner}'


db.connect()
db.create_tables([Cat, Owner])

Cat.delete().execute() # clear the database table -- for testing, careful of deleting later on

george = Owner(name='George')
george.save()
zoe = Cat(name='Zoe', color='Yellow', age=3, owner=george)
zoe.save() # make sure to save

sif = Owner(name='Sif')
sif.save()
phaestus = Cat(name='Phaestus', color='Ginger', age=5, owner=sif)
phaestus.save()
print('CAT WITH OWNER INFO')
print(phaestus)
print(phaestus.owner.name)

salem = Cat(name='Salem', color='Black', age=500)
salem.save()

peaches = Cat(name='Peaches', color='Tabby', age=11)
peaches.save()

cats = Cat.select()  # query object
for cat in cats:
    print(cat)

list_of_cats = list(cats) # regular Python list

"""CRUD Operations
Create - insert
Read - select
Update
Delete
"""

phaestus.age = 7
phaestus.save()

print('After Phaestus age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

# can update many rows if needed
rows_modified = Cat.update(age=6).where(Cat.name == 'Peaches').execute()

print('After Peaches age changed')
cats = Cat.select()
for cat in cats:
    print(cat)

print(f'{rows_modified} row(s) modified')

buzz = Cat(name='Buzz', color='Grey', age=3)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three')

cat_with_s_in_name = Cat.select().where(Cat.name % '*s*')
for cat in cat_with_s_in_name:
    print(cat, 'has s in their name')

cat_with_a_in_name = Cat.select().where(Cat.name.contains('a')) # case insensitive
for cat in cat_with_a_in_name:
    print(cat, 'has a in their name')


salem_from_db = Cat.get_or_none(name='Salem')
print(salem_from_db)

cat_100 = Cat.get_or_none(Cat.id == 100)
print(cat_100)

# count, sort, limit
total = Cat.select().count()
print(total)

total_cats_who_are_5 = Cat.select().where(Cat.age == 5).count()
print(total_cats_who_are_5)

cats_by_name = Cat.select().order_by(Cat.name)
print(list(cats_by_name))

cats_by_age = Cat.select().order_by(Cat.age.desc(), Cat.name.desc())  # first one is prioritized, then sort by next (name)
print(list(cats_by_age))

first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))

# delete
# Cat.delete() # will delete EVERYTHING if no WHERE clause
# print(list(Cat.select()))

rows_delete = Cat.delete().where(Cat.name == 'Buzz')
print(list(Cat.select()))