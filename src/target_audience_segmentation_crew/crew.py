from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
import os
##from langchain_anthropic import ChatAnthropic

##os.environ["ANTHROPIC_API_KEY"] = "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"
os.environ["SERPER_API_KEY"] = "a4532baa46e572bab32d01afbdc8af2f085c664ef718407ffdb941d3028dfd5fcre"
os.environ["ANTHROPIC_API_KEY"] = "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"
##anthropic_api_key = os.environ["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"]
##anthropic_llm= ChatAnthropic(temperature=0.3,model="Claude 3.5 Sonnet 2024-10-22")


@CrewBase
class TargetAudienceSegmentationCrewCrew():
    """TargetAudienceSegmentationCrew crew"""

    @agent
    def analysis_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['analysis_expert'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"),model="anthropic/claude-3-5-sonnet-20241022",)
        )


    @agent
    def segmentation_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['segmentation_specialist'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-5-sonnet-20241022", )
        )

    @agent
    def output_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['output_formatter'],
            llm=LLM(api_key=os.getenv("ANTHROPIC_API_KEY"), model="anthropic/claude-3-5-sonnet-20241022", )
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
