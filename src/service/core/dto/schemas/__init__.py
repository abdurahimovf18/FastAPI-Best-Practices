
# Schemas are centeralized python objects that holds type annotations
# compitable with DTOs or in other words pydantic.BaseModel s with settings prepared
# to work with databases.

# here how the folder structure is created:
# we have models.py where there are database models annotations. to use with DRY

# also other files will contain http clients schemas, for example user.py contains user-service http 
# client schemas which is important to make correct requests as well.
