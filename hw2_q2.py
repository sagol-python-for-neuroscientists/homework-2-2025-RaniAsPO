from collections import namedtuple
from enum import Enum
from itertools import zip_longest

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

# Define the mapping for pair interactions

def get_new_conditions(agent1: Agent, agent2: Agent) -> tuple:
    """
    Determines the new conditions for a pair of agents based on their current categories.
    Handles symmetric cases to improve efficiency.
    """
    category1, category2 = agent1.category, agent2.category

    # If either is a Cure, apply the improvement logic
    if Condition.CURE in {category1, category2}:
        if category1 == Condition.CURE:
            return (category1, improve_condition(category2))
        return (improve_condition(category1), category2)

    # Symmetric deterioration cases
    if {category1, category2} == {Condition.SICK, Condition.DYING}:
        return (Condition.DYING, Condition.DEAD)

    # Both agents are Sick
    if category1 == category2 == Condition.SICK:
        return (Condition.DYING, Condition.DYING)

    # Both agents are Dying
    if category1 == category2 == Condition.DYING:
        return (Condition.DEAD, Condition.DEAD)

def improve_condition(category: Condition) -> Condition:
    """
    Improves the condition of an agent by one step toward health.
    """
    if category == Condition.DYING:
        return Condition.SICK
    if category == Condition.SICK:
        return Condition.HEALTHY
    return category

# Define the main function to model the meeting of agents
def meetup(agent_listing: tuple) -> list:
    """
    Model the outcome of the meetings of pairs of agents.
    """
    # Filter out "Healthy" and "Dead" agents
    active_agents = [agent for agent in agent_listing if agent.category not in {Condition.HEALTHY, Condition.DEAD}]

    # Pair up agents; if there's an odd number, leave the last agent unchanged
    pairs = zip_longest(*[iter(active_agents)] * 2, fillvalue=None)

    updated_agents = []
    for agent1, agent2 in pairs:
        if agent2 is None:  # Handle the odd agent out
            updated_agents.append(agent1)
        else:
            new_cat1, new_cat2 = get_new_conditions(agent1, agent2)
            updated_agents.extend([
                Agent(name=agent1.name, category=new_cat1),
                Agent(name=agent2.name, category=new_cat2),
            ])

    # Include "Healthy" and "Dead" agents as-is in the final output
    unchanged_agents = [agent for agent in agent_listing if agent.category in {Condition.HEALTHY, Condition.DEAD}]
    return updated_agents + unchanged_agents

if __name__ == '__main__':
    # Example input
    agent_listing = (
        Agent("Adam", Condition.SICK),
        Agent("Cure0", Condition.CURE),
        Agent("Cure1", Condition.CURE),
        Agent("Bob", Condition.HEALTHY),
        Agent("Alice", Condition.DEAD),
        Agent("Charlie", Condition.DYING),
        Agent("Vaccine", Condition.SICK),
        Agent("Darlene", Condition.DYING),
        Agent("Emma", Condition.SICK),
        Agent("Cure2", Condition.CURE),
    )

    # Process the meeting
    updated_listing = meetup(agent_listing)

    # Print the result
    print(f"Question 2 solution: {updated_listing}")