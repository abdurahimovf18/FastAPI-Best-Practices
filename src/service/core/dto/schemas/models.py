from typing import Annotated  # noqa: F401

from pydantic import Field  # noqa: F401

# here is quick example for schemas. you can delete this freely and write your own
# Schemas.

"""
import uuid
import re
from typing import Annotated, Any

from pydantic import Field, BaseModel
from pydantic_core import core_schema
from pydantic.json_schema import JsonSchemaValue
from pydantic.annotated_handlers import GetCoreSchemaHandler
from pydantic._internal import _schema_generation_shared


class UsernameStr:
    \"""
    Custom type that ensures a valid username.
    Adjust regex or validation as needed.
    \"""

    _regex = re.compile(r'^[a-zA-Z0-9_.-]{3,32}$')

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source: type[Any],
        _handler: GetCoreSchemaHandler,
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls._validate,
            core_schema.str_schema()
        )

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        core_schema: core_schema.CoreSchema,
        handler: _schema_generation_shared.GetJsonSchemaHandler  # type: ignore
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.update(
            type="string",
            format="username",
            minLength=3,
            maxLength=32,
            pattern=cls._regex.pattern,
            examples=["john_doe", "user.01", "admin-user"]
        )
        return field_schema

    @classmethod
    def _validate(cls, input_value: str, /) -> str:
        if not isinstance(input_value, str):
            raise TypeError("Username must be a string")
        if not cls._regex.fullmatch(input_value):
            raise ValueError(f"Invalid username format: '{input_value}'")
        return input_value


class User:
    id = Annotated[uuid.UUID, Field()]
    username = Annotated[UsernameStr, Field()]


# in this manner, UserDTO will be using User's fields

class UserDTO(BaseModel):
    id: User.id  # in other files it will look like: schema.User.id
    username: User.username
"""
