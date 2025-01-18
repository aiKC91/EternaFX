CHATGPT_PROMPT_DICTIONARY = {
    "general_setup": {
        "description": "Setup prompts for general-purpose ChatGPT configuration or initialization.",
        "examples": [
            "Initialize ChatGPT with memory logging for user interaction.",
            "Configure ChatGPT for modular development in Python."
        ]
    },
    "ai_adventure_platform": {
        "description": "Prompts for building an AI-powered adventure gamification platform.",
        "modules": {
            "adventure_manager": {
                "purpose": "Manages the storyline, quests, and decision-making within the game.",
                "example": "Write a Python class to manage adventure scenes, with methods to add scenes, set a starting scene, and handle user choices."
            },
            "animation_engine": {
                "purpose": "Handles animations for transitions and user actions.",
                "example": "Write a Python class for animations, including a typewriter effect for scene descriptions."
            },
            "user_profile": {
                "purpose": "Manages user stats, inventory, and achievements.",
                "example": "Create a UserProfile class to track health, inventory, and unlocked achievements."
            },
            "utils": {
                "purpose": "Contains helper functions for random events or formatting.",
                "example": "Provide a utility function to simulate a random event with a given probability."
            }
        },
        "example_usage": {
            "description": "Demonstrates how to integrate modules for a playable game.",
            "code": [
                "Define scenes using AdventureManager.",
                "Animate transitions with AnimationEngine.",
                "Track user progress with UserProfile."
            ]
        }
    },
    "logging_and_chat_management": {
        "description": "Prompts for building a modular logging system for ChatGPT conversations.",
        "modules": {
            "logger": {
                "purpose": "Handles persistent logging of messages to a file.",
                "example": "Create a ChatLogger class to log messages with timestamps to a text file."
            },
            "chat_session": {
                "purpose": "Manages in-memory chat history and integrates with the logger.",
                "example": "Create a ChatSession class to track the conversation and log each message."
            },
            "utils": {
                "purpose": "Provides utility functions for timestamp formatting or data validation.",
                "example": "Write a function to return the current timestamp in 'YYYY-MM-DD HH:MM:SS' format."
            }
        },
        "example_usage": {
            "description": "Shows how to log and manage chat sessions.",
            "code": [
                "Initialize ChatLogger with a log file.",
                "Create a ChatSession instance linked to the logger.",
                "Log messages and retrieve chat history."
            ]
        }
    },
    "interactive_visualizations": {
        "description": "Prompts for creating interactive 3D visualizations using Plotly and mathematical functions.",
        "modules": {
            "zeta_function_plot": {
                "purpose": "Generates a 3D plot of the Riemann zeta function's absolute values and highlights critical zeros.",
                "example": "Write a Python function using Plotly to plot |ζ(s)| for Re(s) ∈ [0.1, 0.99] and Im(s) ∈ [0, 50]."
            },
            "enhancements": {
                "description": "Suggestions for improving visualizations.",
                "examples": [
                    "Add hover tooltips displaying values at critical points.",
                    "Use dynamic color scales for better contrast."
                ]
            }
        },
        "example_usage": {
            "description": "Shows how to generate and display the zeta function dynamics.",
            "code": [
                "Define the grid for Re(s) and Im(s).",
                "Compute |ζ(s)| and plot it as a surface with critical zeros highlighted.",
                "Customize layout with axis labels and titles."
            ]
        }
    },
    "modular_development_principles": {
        "description": "General prompts and principles for modular software development.",
        "examples": [
            "How to design a modular Python application with separate files for core functionality, utilities, and configuration.",
            "Best practices for creating reusable and extensible classes."
        ]
    },
    "extensions_and_scalability": {
        "description": "Prompts for adding advanced features or making the platform scalable.",
        "ideas": [
            "Implement log rotation for large log files.",
            "Add GPT integration to dynamically generate scene descriptions or dialogue.",
            "Integrate a persistent save system using JSON or databases.",
            "Enhance animations with graphical libraries like Pygame."
        ]
    }
}