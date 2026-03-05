"""
EcoNexo AI Agent Module
Implements ReAct architecture with tools, memory, and observability
Based on AI Agents roadmap best practices
"""

import os
import time
import json
from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
from enum import Enum


class AgentState(Enum):
    """Agent execution states"""
    IDLE = "idle"
    PERCEIVING = "perceiving"
    REASONING = "reasoning"
    ACTING = "acting"
    OBSERVING = "observing"
    REFLECTING = "reflecting"
    ERROR = "error"


@dataclass
class ToolDefinition:
    """Defines an agent tool/action"""
    name: str
    description: str
    function: Callable
    input_schema: Dict[str, Any]
    examples: List[str]
    error_handling: Optional[Callable] = None


@dataclass
class AgentMemory:
    """Agent memory structure"""
    short_term: List[Dict[str, Any]]  # Recent interactions
    long_term: Dict[str, Any]  # Persistent knowledge
    episodic: List[Dict[str, Any]]  # Event history
    semantic: Dict[str, Any]  # Factual knowledge


class ProductivityAgent:
    """
    ReAct-based AI Agent for productivity coaching
    
    Architecture:
    1. Perception: Receive user input
    2. Reasoning: Analyze context and plan
    3. Action: Execute tools/functions
    4. Observation: Process results
    5. Reflection: Learn and adapt
    """
    
    def __init__(self, user_profile: Dict[str, Any], api_key: str = None):
        self.user_profile = user_profile
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.state = AgentState.IDLE
        self.tools: Dict[str, ToolDefinition] = {}
        self.memory = AgentMemory(
            short_term=[],
            long_term={},
            episodic=[],
            semantic={}
        )
        self.execution_log = []
        
        # Register default tools
        self._register_default_tools()
    
    def _register_default_tools(self):
        """Register built-in productivity tools"""
        
        # Task breakdown tool
        self.register_tool(ToolDefinition(
            name="break_down_task",
            description="Break a large task into smaller, actionable steps",
            function=self._break_down_task,
            input_schema={
                "type": "object",
                "properties": {
                    "task": {"type": "string", "description": "The task to break down"},
                    "num_steps": {"type": "integer", "description": "Desired number of steps"}
                },
                "required": ["task"]
            },
            examples=[
                "Break down: Write a research paper",
                "Break down: Launch a new product"
            ]
        ))
        
        # Pomodoro timer tool
        self.register_tool(ToolDefinition(
            name="create_pomodoro_plan",
            description="Create a Pomodoro technique schedule for focused work",
            function=self._create_pomodoro_plan,
            input_schema={
                "type": "object",
                "properties": {
                    "task": {"type": "string"},
                    "duration_minutes": {"type": "integer", "default": 120}
                },
                "required": ["task"]
            },
            examples=["Create Pomodoro plan for: Deep work session"]
        ))
        
        # Priority matrix tool
        self.register_tool(ToolDefinition(
            name="prioritize_tasks",
            description="Prioritize tasks using Eisenhower Matrix (urgent/important)",
            function=self._prioritize_tasks,
            input_schema={
                "type": "object",
                "properties": {
                    "tasks": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["tasks"]
            },
            examples=["Prioritize: ['email', 'project deadline', 'meeting', 'learning']"]
        ))
        
        # Productivity insights tool
        self.register_tool(ToolDefinition(
            name="analyze_productivity_pattern",
            description="Analyze user's productivity patterns and suggest improvements",
            function=self._analyze_productivity,
            input_schema={
                "type": "object",
                "properties": {
                    "profile_type": {"type": "string"},
                    "completed_tasks": {"type": "integer"}
                },
                "required": ["profile_type"]
            },
            examples=["Analyze productivity for Executor profile"]
        ))
    
    def register_tool(self, tool: ToolDefinition):
        """Register a new tool for the agent"""
        self.tools[tool.name] = tool
        self._log_event("tool_registered", {"tool_name": tool.name})
    
    def _break_down_task(self, task: str, num_steps: int = 5) -> Dict[str, Any]:
        """Break down a task into steps based on user profile"""
        profile_type = self.user_profile.get("profile", "Executor")
        
        # Profile-specific breakdown strategies
        strategies = {
            "Executor": [
                f"1. Identify the quickest win in: {task}",
                f"2. Execute the simplest component immediately",
                f"3. Build momentum with next micro-task",
                f"4. Track visible progress",
                f"5. Complete and celebrate"
            ],
            "Organizador": [
                f"1. Define clear success criteria for: {task}",
                f"2. Create detailed checklist of requirements",
                f"3. Allocate time blocks in calendar",
                f"4. Set up tracking system",
                f"5. Execute systematically step-by-step"
            ],
            "Criativo": [
                f"1. Brainstorm multiple approaches to: {task}",
                f"2. Sketch out innovative solution pathways",
                f"3. Prototype the most interesting idea",
                f"4. Iterate and refine based on feedback",
                f"5. Finalize with creative polish"
            ]
        }
        
        # Fallback for English profiles
        if profile_type not in strategies:
            if "Executor" in profile_type:
                profile_type = "Executor"
            elif "Organizer" in profile_type or "Organizador" in profile_type:
                profile_type = "Organizador"
            elif "Creative" in profile_type or "Criativo" in profile_type:
                profile_type = "Criativo"
            else:
                profile_type = "Executor"
        
        steps = strategies.get(profile_type, strategies["Executor"])
        
        return {
            "task": task,
            "profile_optimized": profile_type,
            "steps": steps[:num_steps],
            "estimated_time": f"{num_steps * 25} minutes (using Pomodoro)"
        }
    
    def _create_pomodoro_plan(self, task: str, duration_minutes: int = 120) -> Dict[str, Any]:
        """Create Pomodoro schedule"""
        num_pomodoros = duration_minutes // 25
        
        schedule = []
        current_time = 0
        
        for i in range(num_pomodoros):
            schedule.append({
                "block": i + 1,
                "type": "focus",
                "duration": 25,
                "start_min": current_time,
                "activity": f"{task} - Focus session {i + 1}"
            })
            current_time += 25
            
            # Add break
            break_duration = 15 if (i + 1) % 4 == 0 else 5
            schedule.append({
                "block": f"{i + 1}b",
                "type": "break",
                "duration": break_duration,
                "start_min": current_time,
                "activity": "Long break" if break_duration == 15 else "Short break"
            })
            current_time += break_duration
        
        return {
            "task": task,
            "total_duration": current_time,
            "focus_blocks": num_pomodoros,
            "schedule": schedule,
            "tips": [
                "🔕 Eliminate all distractions during focus blocks",
                "✅ Mark completion after each Pomodoro",
                "🚶 Stand up and move during breaks"
            ]
        }
    
    def _prioritize_tasks(self, tasks: List[str]) -> Dict[str, Any]:
        """Prioritize using Eisenhower Matrix"""
        # Simple heuristic-based prioritization
        # In production, this could use ML or user input
        
        matrix = {
            "do_first": [],      # Urgent & Important
            "schedule": [],      # Not Urgent & Important
            "delegate": [],      # Urgent & Not Important
            "eliminate": []      # Not Urgent & Not Important
        }
        
        urgent_keywords = ["deadline", "urgent", "asap", "today", "now", "meeting"]
        important_keywords = ["project", "goal", "strategic", "learning", "health"]
        
        for task in tasks:
            task_lower = task.lower()
            is_urgent = any(kw in task_lower for kw in urgent_keywords)
            is_important = any(kw in task_lower for kw in important_keywords)
            
            if is_urgent and is_important:
                matrix["do_first"].append(task)
            elif is_important:
                matrix["schedule"].append(task)
            elif is_urgent:
                matrix["delegate"].append(task)
            else:
                matrix["eliminate"].append(task)
        
        return {
            "matrix": matrix,
            "recommendation": matrix["do_first"][0] if matrix["do_first"] else 
                            matrix["schedule"][0] if matrix["schedule"] else
                            "No high-priority tasks identified",
            "next_actions": matrix["do_first"][:3] if matrix["do_first"] else matrix["schedule"][:3]
        }
    
    def _analyze_productivity(self, profile_type: str, completed_tasks: int = 0) -> Dict[str, Any]:
        """Analyze productivity patterns"""
        
        insights = {
            "Executor": {
                "strength": "Quick action and implementation",
                "risk": "May skip planning, leading to rework",
                "optimization": "Add 5-min planning before each task",
                "ideal_workflow": "Pomodoro technique with clear micro-goals"
            },
            "Organizador": {
                "strength": "Systematic approach and thoroughness",
                "risk": "Over-planning can delay action",
                "optimization": "Set 'planning time limit' before execution",
                "ideal_workflow": "Time-blocking with detailed checklists"
            },
            "Criativo": {
                "strength": "Innovation and flexible thinking",
                "risk": "May get distracted by new ideas",
                "optimization": "Capture ideas in 'idea parking lot', focus on current task",
                "ideal_workflow": "Creative sprints followed by structured refinement"
            }
        }
        
        # Normalize profile key
        for key in insights.keys():
            if key.lower() in profile_type.lower():
                profile_type = key
                break
        
        profile_insight = insights.get(profile_type, insights["Executor"])
        
        # Calculate productivity score
        iap_score = self.user_profile.get("iap_score", 0)
        
        return {
            "profile": profile_type,
            "completed_tasks": completed_tasks,
            "iap_score": iap_score,
            "insights": profile_insight,
            "suggestions": [
                f"Your {profile_insight['strength']} is a key asset",
                f"Watch out for: {profile_insight['risk']}",
                f"Try this: {profile_insight['optimization']}"
            ],
            "performance_trend": "improving" if completed_tasks >= 2 else "needs focus"
        }
    
    def _log_event(self, event_type: str, data: Dict[str, Any]):
        """Log agent events for observability"""
        log_entry = {
            "timestamp": time.time(),
            "event": event_type,
            "state": self.state.value,
            "data": data
        }
        self.execution_log.append(log_entry)
        
        # Keep only last 100 events
        if len(self.execution_log) > 100:
            self.execution_log = self.execution_log[-100:]
    
    def _update_memory(self, interaction: Dict[str, Any], memory_type: str = "short_term"):
        """Update agent memory"""
        if memory_type == "short_term":
            self.memory.short_term.append(interaction)
            # Keep last 10 interactions
            if len(self.memory.short_term) > 10:
                self.memory.short_term = self.memory.short_term[-10:]
        
        elif memory_type == "episodic":
            self.memory.episodic.append(interaction)
        
        elif memory_type == "semantic":
            key = interaction.get("key")
            if key:
                self.memory.semantic[key] = interaction.get("value")
    
    def reason_and_plan(self, user_input: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reasoning phase: analyze input and create action plan
        Uses Chain-of-Thought approach
        """
        self.state = AgentState.REASONING
        self._log_event("reasoning_started", {"input": user_input})
        
        # Check if tools are needed
        tool_suggestions = []
        
        if any(keyword in user_input.lower() for keyword in ["break down", "steps", "how to"]):
            tool_suggestions.append("break_down_task")
        
        if any(keyword in user_input.lower() for keyword in ["schedule", "plan", "time"]):
            tool_suggestions.append("create_pomodoro_plan")
        
        if any(keyword in user_input.lower() for keyword in ["priority", "prioritize", "important"]):
            tool_suggestions.append("prioritize_tasks")
        
        if any(keyword in user_input.lower() for keyword in ["productivity", "performance", "improve"]):
            tool_suggestions.append("analyze_productivity_pattern")
        
        reasoning = {
            "intent": self._classify_intent(user_input),
            "suggested_tools": tool_suggestions,
            "requires_action": len(tool_suggestions) > 0,
            "context_summary": {
                "profile": self.user_profile.get("profile", "Unknown"),
                "iap": self.user_profile.get("iap_score", 0),
                "recent_interactions": len(self.memory.short_term)
            }
        }
        
        self._log_event("reasoning_completed", reasoning)
        return reasoning
    
    def _classify_intent(self, user_input: str) -> str:
        """Classify user intent"""
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in ["how", "what", "why", "explain"]):
            return "information_seeking"
        elif any(word in input_lower for word in ["break", "divide", "steps"]):
            return "task_breakdown"
        elif any(word in input_lower for word in ["schedule", "plan", "organize"]):
            return "planning"
        elif any(word in input_lower for word in ["priority", "important", "urgent"]):
            return "prioritization"
        elif any(word in input_lower for word in ["help", "stuck", "problem"]):
            return "problem_solving"
        else:
            return "general_inquiry"
    
    def execute_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """Execute a registered tool"""
        self.state = AgentState.ACTING
        self._log_event("tool_execution_started", {"tool": tool_name, "args": kwargs})
        
        start_time = time.time()
        
        try:
            tool = self.tools.get(tool_name)
            if not tool:
                raise ValueError(f"Tool '{tool_name}' not found")
            
            result = tool.function(**kwargs)
            exec_time = (time.time() - start_time) * 1000
            
            self._log_event("tool_execution_completed", {
                "tool": tool_name,
                "success": True,
                "exec_time_ms": exec_time
            })
            
            return {
                "success": True,
                "result": result,
                "execution_time_ms": exec_time
            }
        
        except Exception as e:
            exec_time = (time.time() - start_time) * 1000
            self.state = AgentState.ERROR
            
            self._log_event("tool_execution_failed", {
                "tool": tool_name,
                "error": str(e),
                "exec_time_ms": exec_time
            })
            
            if tool and tool.error_handling:
                return tool.error_handling(e, kwargs)
            
            return {
                "success": False,
                "error": str(e),
                "execution_time_ms": exec_time
            }
    
    def get_tool_descriptions(self) -> str:
        """Get formatted tool descriptions for LLM"""
        descriptions = []
        for name, tool in self.tools.items():
            descriptions.append(f"- **{name}**: {tool.description}")
        return "\n".join(descriptions)
    
    def get_execution_summary(self) -> Dict[str, Any]:
        """Get summary of agent execution"""
        return {
            "current_state": self.state.value,
            "tools_available": len(self.tools),
            "memory_short_term": len(self.memory.short_term),
            "memory_episodic": len(self.memory.episodic),
            "execution_log_size": len(self.execution_log),
            "recent_events": self.execution_log[-5:] if self.execution_log else []
        }


# Utility functions for integration
def create_agent_from_profile(user_profile: Dict[str, Any]) -> ProductivityAgent:
    """Factory function to create agent with user profile"""
    return ProductivityAgent(user_profile)


def enhance_llm_with_tools(agent: ProductivityAgent, user_input: str) -> str:
    """
    Enhance LLM response with tool execution
    Implements basic ReAct loop
    """
    # Reason
    reasoning = agent.reason_and_plan(user_input, {})
    
    # Act if tools suggested
    tool_results = []
    if reasoning["suggested_tools"]:
        for tool_name in reasoning["suggested_tools"][:2]:  # Limit to 2 tools
            # Extract parameters from input (simplified)
            if tool_name == "break_down_task":
                # Try to extract task from input
                task = user_input
                result = agent.execute_tool(tool_name, task=task)
                tool_results.append(result)
            
            elif tool_name == "analyze_productivity_pattern":
                result = agent.execute_tool(
                    tool_name,
                    profile_type=agent.user_profile.get("profile", "Executor"),
                    completed_tasks=agent.user_profile.get("tasks_completed", 0)
                )
                tool_results.append(result)
    
    # Format tool results for LLM context
    tools_context = ""
    if tool_results:
        tools_context = "\n\n**Tool Results:**\n"
        for i, result in enumerate(tool_results):
            if result["success"]:
                tools_context += f"\n{i+1}. {json.dumps(result['result'], indent=2)}\n"
    
    return tools_context
