from pydantic import BaseModel, Field
from typing import Type
from langchain.tools import BaseTool

class GenerateProfileSchema(BaseModel):
    name: str = Field(..., description="name of user")
    favorites: str = Field(..., description="favorite of user")
    dislikes: str = Field(..., description="dislikes of user")


class GenerateProfileTool(BaseTool):
    name = "generate_profile"
    description = "Use this tool to generate a profile."
    args_schema: Type[GenerateProfileSchema] = GenerateProfileSchema

    def _run(
        self,
        name,
        favorites,
        dislikes,
    ):
        print("generating profile")
        return {
            "name": name,
            "favorites": favorites,
            "dislikes": dislikes,
        }

    async def _arun(
        self,
        name,
        favorites,
        dislikes,
    ):
        raise NotImplementedError("Not implemented yet")
