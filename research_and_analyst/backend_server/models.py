# models.py
import operator
from typing import Annotated, List
from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# -------------------------------
# Section Model
# -------------------------------

class Section(BaseModel):
    """
    Represents a section of a research paper.
    """
    title: str = Field(..., description="Title of the section")
    content: str = Field(..., description="Content of the section")
    # keywords: List[str] = Field(..., description="Keywords related to the section")
    # references: List[str] = Field(..., description="References related to the section")

# -------------------------------
# Analyst Models
# -------------------------------

class Analyst(BaseModel):
    """
    Represents an analyst with their name and expertise.
    """
    affiliation: str = Field(description="Primary affiliation of the analyst")
    name: str = Field(description="Name of the analyst")
    role: str = Field(description="Role of the analyst in the context of the topic")
    description: str = Field(
        description="Description of the analyst's focus, concerns, and motives"
    )

    @property
    def persona(self) -> str:
        """
        Returns a string representation of the analyst's persona.
        """
        return (
            f"Name: {self.name}\n"
            f"Role: {self.role}\n"
            f"Affiliation: {self.affiliation}"
            f"Description: {self.description}"
        )
    
    class Perspectives(BaseModel):
        analysts: List[Analyst] = Field(
            description="Comprehensive list of analysts with their roles and affiliations"
        )

# -------------------------------
# Search Query Output Parser
# -------------------------------

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Search query string generated for retrieving relevant documents")

# -------------------------------
# State Classes for Graphs
# -------------------------------

class GebnerateAnalystsState(TypedDict):
    topic: str # Research topic
    max_analysts: int # Maximum number of analysts to generate
    human_analyst_feedback: str # Feedback from the human analyst
    analysts: List[Analyst] # List of generated analysts

class InterviewState(MessagesState):
    max_num_turns: int  # Max interview turns allowed
    context: Annotated[list, operator.add]  # Retrieved or searched context
    analyst: Analyst  # Analyst conducting interview
    interview: str  # Full interview transcript
    sections: list  # Generated section from interview

class ResearchGraphState(TypedDict):
    topic: str # Research topic
    max_analysts: int # Maximum number of analysts to generate
    human_analyst_feedback: str # Feedback from the human analyst
    analysts: List[Analyst] # List of generated analysts
    sections: Annotated[list, operator.add]  # All interview-generated sections
    introduction: str  # Introduction of final report
    content: str  # Main content of report
    conclusion: str  # Conclusion of final report
    final_report: str  # Compiled report string