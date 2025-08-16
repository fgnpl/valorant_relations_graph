# Valorant Relations Visualizer  

![Valorant Agents Network](https://img.shields.io/badge/game-Valorant-red) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![NetworkX](https://img.shields.io/badge/library-NetworkX-green) ![PyVis](https://img.shields.io/badge/library-PyVis-orange)  

A Python-based interactive relationship visualizer for Valorant agents, representing their connections (as of patch 6.04) as an interactive graph network.  

## Features  
- Visualize relationships between Valorant agents (Friends, Enemies, Neutral, Romantic)  
- Interactive graph with different colored edges for relationship types  
- Subgraph generation to explore connections from a specific agent  
- Directed & undirected relationships (one-sided or mutual)  
- Easy-to-use CLI for adding agents and relationships  

## Relationship Types  
| Color  | Relationship Type |  
|--------|------------------|  
| Green  | Friends          |  
| Blue   | Enemies          |  
| Yellow | Neutral          |  
| Pink   | Romantic         |  

![Logo](assets/valorant_graph.png)

## Usage  
Run the script and use the following commands:  

### Commands  
| Command | Description | Example |  
|---------|-------------|---------|  
| add_person("Agent") | Add a new agent | add_person("Jett") |  
| add_connection("Agent1", "Agent2", "Status", "Direction") | Define a relationship | add_connection("Jett", "Phoenix", "Friends", "Undirected") |  
| create_subgraph("Agent") | Show connections from an agent | create_subgraph("Sage") |  
| get_adjacent("Agent") | List connected agents | get_adjacent("Reyna") |  
| show_graph() | Display full relationship graph | show_graph() |  
| exit | Quit the program | exit |  

### Example  
```python
add_person("Jett")  
add_person("Phoenix")  
add_connection("Jett", "Phoenix", "Friends", "Undirected")  
show_graph()
