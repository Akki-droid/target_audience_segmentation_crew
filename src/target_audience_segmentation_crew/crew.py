from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

from langchain.llms import OpenAI
import os

# Set environment variables
#os.environ["SERPER_API_KEY"] = "cd15c425b992781c8651a142e33ca2a9b96ca85e7e582b3f0b87e14983ca46ba"
#os.environ["OPENAI_API_KEY"] = "UYvKT8SQgeaXQcLMeJ9lLLlyTEjeijHUwKhncHYqrYs0ZWIw9VNj4pVGMA"


@CrewBase
class TargetAudienceSegmentationCrewCrew():
    """TargetAudienceSegmentationCrew crew"""

    @agent
    def analysis_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['analysis_expert'],
            
        )

    @agent
    def segmentation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['segmentation_specialist'],
            
        )

    @agent
    def output_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['output_formatter'],
            
        )


    @task
    def analyze_business_and_products_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_business_and_products_task'],
            tools=[SerperDevTool()],
        )

    @task
    def identify_primary_segments_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_primary_segments_task'],
            tools=[],
        )

    @task
    def identify_secondary_segments_task(self) -> Task:
        return Task(
            config=self.tasks_config['identify_secondary_segments_task'],
            tools=[],
        )

    @task
    def format_output_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_output_task'],
            tools=[],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the TargetAudienceSegmentationCrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
