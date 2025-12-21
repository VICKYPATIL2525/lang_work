# LangGraph Workshop Project

A comprehensive educational workshop project demonstrating LangGraph (LLM-Graph) concepts with practical examples and real-world applications.

## 📋 Project Overview

This project is designed to teach participants how to use **LangGraph** - a powerful framework for building structured AI workflows using Large Language Models (LLMs). Through progressive examples, from simple to complex workflows, you'll master:

- State management in graph workflows
- Sequential and parallel node execution
- Conditional routing and branching
- Human-in-the-loop interactions
- Multi-database integration with LLM-driven routing

**Perfect for**: Developers, data scientists, and AI engineers learning workflow orchestration with LLMs.

---

## 🎯 Quick Start

### Prerequisites

- Python 3.8+
- Azure OpenAI account (for LLM features)
- MongoDB (for database examples)
- SQLite (included with Python)

### 1. Setup Virtual Environment

```bash
# Activate the virtual environment
myenv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install langgraph langchain langchain-openai pymongo python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_VERSION=2024-12-01-preview
```

### 4. Setup Databases (Optional)

```bash
# Setup SQLite
python seed_sqlite.py

# Setup MongoDB
python seed_mongo.py
```

### 5. Run Your First Example

```bash
python test0.py
```

---

## 📚 Tutorial Examples

The project contains 6 progressive examples, each demonstrating key LangGraph concepts:

### Example 0: Basic Addition Workflow ⭐ (Beginner)

**Files**: `test0.py`, `test0_commented_v1.py`

**What You'll Learn**:
- Creating a StateGraph
- Defining state structure with TypedDict
- Building nodes (processing functions)
- Connecting nodes with edges
- Compiling and executing workflows

**Workflow**:
```
START → [add node] → END
```

**Example**:
```python
python test0.py
# Input: num1=5, num2=5
# Output: result=10
```

---

### Example 1: LLM Q&A System ⭐⭐ (Beginner/Intermediate)

**File**: `test1_commented_v1.py`

**What You'll Learn**:
- Integrating Azure OpenAI with LangGraph
- Making external API calls from nodes
- Prompt engineering
- Response parsing

**Workflow**:
```
START → [llm_qa node] → END
```

**Example**:
```python
python test1_commented_v1.py
# Input: "How far is the moon from earth?"
# Output: "The Moon is approximately 384,400 kilometers..."
```

**Key Concepts**:
- LLM integration
- State enrichment with AI-generated content
- Environment variable management

---

### Example 2: Sequential Blog Generation ⭐⭐⭐ (Intermediate)

**Files**: `test2.py`, `test2_commented_v1.py`

**What You'll Learn**:
- Chaining multiple LLM calls
- State evolution through nodes
- Using output from one node as input to the next
- Building multi-step workflows

**Workflow**:
```
START → [outline_generator] → [content_generator] → END
```

**Example**:
```python
python test2.py
# Input: title="The Future of Artificial Intelligence"
# Step 1: Generate outline
# Step 2: Generate full blog using outline
# Output: Complete blog post with title, outline, and content
```

**Key Concepts**:
- Sequential chaining
- State accumulation
- Multi-step content generation

---

### Example 3: Parallel LLM Analysis ⭐⭐⭐⭐ (Advanced)

**Files**: `test3.py`, `test3_commented_v1.py`

**What You'll Learn**:
- Running multiple nodes in parallel
- Node specialization (each node focused on one task)
- Partial state updates
- Automatic state merging
- Synchronization and result aggregation

**Workflow**:
```
        [START]
       /   |   \
      /    |    \
     ↓     ↓     ↓
  [Grammar] [Sentiment] [Clarity]   ← All run in parallel!
     \     |     /
      \    |    /
       \   |   /
        ↓ ↓ ↓
     [Finalizer]
        ↓
       [END]
```

**Example**:
```python
python test3.py
# Analyzes essay on three dimensions simultaneously:
# - Grammar Score: 92/100
# - Sentiment Score: 85/100
# - Clarity Score: 88/100
# Generates comprehensive analysis report
```

**Key Concepts**:
- True parallel execution
- Efficiency gains
- State merging for concurrent operations
- Building scalable workflows

---

### Example 4: Conditional Routing ⭐⭐⭐ (Intermediate)

**File**: `test4_commented_v1.py`

**What You'll Learn**:
- Conditional edges and branching
- Decision functions
- Dynamic routing based on state
- Handling multiple workflow paths

**Workflow**:
```
START → [check_feedback] →
            ├─(positive)→ [thank_you] → END
            └─(negative)→ [apology] → END
```

**Example**:
```python
python test4_commented_v1.py
# Positive feedback: "I love this product!"
# Path: check → thank → END
# Response: Thank you message

# Negative feedback: "This product is terrible!"
# Path: check → apology → END
# Response: Apology message
```

**Key Concepts**:
- Dynamic workflow routing
- Conditional logic
- Multiple workflow branches
- Context-aware responses

---

### Example 5: Human-in-the-Loop Iterative Workflow ⭐⭐⭐⭐ (Advanced)

**Files**: `test5.py`, `test5_commented_v1.py`

**What You'll Learn**:
- Pausing workflow for human approval
- Iterative refinement loops
- Feedback integration
- Attempt tracking
- Loop breaking conditions

**Workflow**:
```
START → [generate] → [approval] →
          ↑           ↓ (if approved → END)
          └───────────┘ (if not approved → loop back)
```

**Example**:
```python
python test5.py
# Iteration 1:
#   Generated: "Smart Watch - A wearable device"
#   Human: "No, make it more appealing"
# Iteration 2:
#   Generated: "Smart Watch - Advanced wearable..."
#   Human: "Yes, approved!"
# Result: Final description accepted
```

**Key Concepts**:
- Interactive workflows
- Feedback loops
- Iterative improvement
- User engagement with AI

---

## 🔗 Advanced: Multi-Source Database Integration

**File**: `multisource_langgraph.py`

**What You'll Learn**:
- LLM-driven intent recognition
- Multi-database routing
- Query execution across different sources
- Combining data from multiple databases
- Production-ready patterns

**Features**:
- Intent-based query routing
- MongoDB support (student info, hostel data)
- SQLite support (exam results, timetable)
- Natural language to database translation

**Workflow**:
```
START → [planner (intent)] → [executor (db query)] → [finalizer (response)] → END
```

**Example Queries**:
```bash
python multisource_langgraph.py

> Ask: What is the hostel room for Rohit Kumar?
Planner: {"source": "mongo", "action": "get_hostel", "student_name": "Rohit Kumar"}
Result: Rohit Kumar is assigned to hostel room A-101

> Ask: Which students have pending fees?
Planner: {"source": "mongo", "action": "pending_fees"}
Result: Lists all students with pending fees status

> Ask: List the top 3 scorers
Planner: {"source": "sqlite", "action": "top_scorers", "limit": 3}
Result: Top 3 performing students with scores

> Ask: Show the timetable for MCA
Planner: {"source": "sqlite", "action": "timetable"}
Result: MCA course schedule
```

**Supported Intents**:

| Query Type | Source | Action | Example |
|-----------|--------|--------|---------|
| Hostel Room | MongoDB | get_hostel | "What hostel room for [student]?" |
| Pending Fees | MongoDB | pending_fees | "List pending fee students" |
| Top Scorers | SQLite | top_scorers | "List top 3 scorers" |
| Timetable | SQLite | timetable | "Show MCA timetable" |

---

## 📁 Project Structure

```
lang_work/
├── README.md                          ← You are here
├── info.txt                           ← Detailed documentation
│
├── 📂 Tutorial Examples
├── test0.py                           (Basic Addition - Simple)
├── test0_commented_v1.py             (Basic Addition - Detailed)
├── test1_commented_v1.py             (LLM Q&A)
├── test2.py                          (Blog Generation - Simple)
├── test2_commented_v1.py             (Blog Generation - Detailed)
├── test3.py                          (Parallel Analysis - Simple)
├── test3_commented_v1.py             (Parallel Analysis - Detailed)
├── test4_commented_v1.py             (Conditional Routing)
├── test5.py                          (Human-in-the-Loop - Simple)
├── test5_commented_v1.py             (Human-in-the-Loop - Detailed)
│
├── 📂 Advanced Integration
├── multisource_langgraph.py          (Multi-DB with LLM routing)
├── questions.json                    (Test questions)
│
├── 📂 Database Setup
├── seed_sqlite.py                    (Create SQLite database)
├── seed_mongo.py                     (Create MongoDB collections)
├── read_sql.py                       (Display SQLite data)
├── read_mongo.py                     (Display MongoDB data)
├── mongo_conn_test.py                (Test MongoDB connection)
├── institute.db                      (SQLite database file)
│
├── 📂 Documentation
├── workflow_diagrams/                (PNG diagrams for each example)
└── Canteen_Information.pdf          (Reference document)
```

---

## 🛠️ Setting Up Databases

### MongoDB Setup

1. **Start MongoDB**:
   ```bash
   # If MongoDB is installed locally
   mongod
   ```

2. **Seed the database**:
   ```bash
   python seed_mongo.py
   ```

3. **View the data**:
   ```bash
   python read_mongo.py
   ```

**Collections Created**:
- `students`: 15 student records with hostel room and fee status
- `faculty`: Faculty members and their subjects
- `attendance`: Student attendance records

### SQLite Setup

1. **Create the database**:
   ```bash
   python seed_sqlite.py
   ```

2. **View the data**:
   ```bash
   python read_sql.py
   ```

**Tables Created**:
- `courses`: BCA, MCA, BSc AI
- `subjects`: Course-wise subjects
- `exam_results`: Student exam scores
- `timetable`: Class schedules

---

## 🎓 Recommended Learning Path

### Day 1: Fundamentals (1-2 hours)
- [ ] Run `test0.py`
- [ ] Study `test0_commented_v1.py` in detail
- [ ] Understand: State, nodes, edges, compilation, execution

### Day 2: LLM Integration (1-2 hours)
- [ ] Configure `.env` with Azure credentials
- [ ] Run `test1_commented_v1.py`
- [ ] Experiment with different questions

### Day 3: Sequential Workflows (1-2 hours)
- [ ] Run `test2.py` and `test2_commented_v1.py`
- [ ] Understand state evolution
- [ ] Modify prompts to generate different content

### Day 4: Parallel Processing (1.5-2 hours)
- [ ] Run `test3.py` and `test3_commented_v1.py`
- [ ] Understand parallel execution
- [ ] Analyze the performance benefits

### Day 5: Advanced Patterns (2-3 hours)
- [ ] Run `test4_commented_v1.py` (conditional routing)
- [ ] Run `test5_commented_v1.py` (human-in-the-loop)
- [ ] Understand interactive workflows

### Day 6: Real-World Application (2-3 hours)
- [ ] Setup databases with `seed_sqlite.py` and `seed_mongo.py`
- [ ] Run `multisource_langgraph.py`
- [ ] Test with various natural language queries
- [ ] Design your own workflow

---

## 🔑 Key Concepts

### State
A TypedDict that defines data flowing through the graph. Persists across all nodes.

```python
class BlogState(TypedDict):
    title: str       # Input
    outline: str     # Generated by first node
    content: str     # Generated by second node
```

### Node
A function that processes the state and returns updates.

```python
def generate_outline(state: BlogState) -> BlogState:
    title = state['title']
    outline = llm.invoke(f"Create outline for: {title}")
    state['outline'] = outline
    return state
```

### Edge
Connection between nodes defining execution flow.

```python
graph.add_edge(START, 'outline_generator')
graph.add_edge('outline_generator', 'content_generator')
graph.add_edge('content_generator', END)
```

### Workflow
Compiled, executable version of the graph.

```python
workflow = graph.compile()
result = workflow.invoke(initial_state)
```

### Parallel Execution
Multiple nodes starting from the same predecessor.

```python
# All three nodes run simultaneously
graph.add_edge(START, "grammar")
graph.add_edge(START, "sentiment")
graph.add_edge(START, "clarity")
```

### Conditional Routing
Branching based on state values.

```python
def decide_next(state):
    if state['sentiment'] == "positive":
        return "thank"
    else:
        return "apology"

graph.add_conditional_edges("check", decide_next, ...)
```

---

## 💡 Practical Exercises

### Exercise 1: Modify Addition
Change `test0.py` to perform **multiplication** instead of addition.

### Exercise 2: Extend Q&A
Add a **follow-up question node** to `test1_commented_v1.py`.

### Exercise 3: Add Blog Editor
Create a new `editor` node in `test2.py` to improve generated content.

### Exercise 4: New Analysis Dimension
Add an **originality analysis** node parallel to others in `test3.py`.

### Exercise 5: More Feedback Categories
Extend `test4.py` to handle **neutral sentiment** with distinct response.

### Exercise 6: Quality Metrics
Add **quality scoring** to `test5.py` that auto-approves high-quality content.

### Exercise 7: Custom Database Query
Add a new intent type to `multisource_langgraph.py` for different database queries.

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langgraph'"
**Solution**: Activate virtual environment and install dependencies
```bash
myenv\Scripts\activate
pip install langgraph langchain langchain-openai
```

### Issue: Azure OpenAI connection errors
**Solution**: Check `.env` file
```bash
# Verify these are set correctly:
# OPENAI_API_KEY
# AZURE_OPENAI_ENDPOINT
# AZURE_OPENAI_VERSION
```

### Issue: MongoDB connection refused
**Solution**: Start MongoDB server
```bash
mongod
```

### Issue: LLM returns non-JSON in planner
**Solution**: Increase prompt clarity in `multisource_langgraph.py`
```python
prompt = "Respond with ONLY valid JSON, NO other text..."
```

### Issue: Infinite loop in test5
**Solution**: Auto-approval is implemented after 3 attempts by default

---

## 📊 Architecture Patterns Demonstrated

| Pattern | Example | Use Case |
|---------|---------|----------|
| **Sequential** | Test 2 | Multi-step content generation |
| **Parallel** | Test 3 | Independent analyses on same data |
| **Conditional** | Test 4 | Different paths based on conditions |
| **Iterative** | Test 5 | Refinement loops with feedback |
| **Intent-driven** | Multi-DB | Smart routing and execution |

---

## 🚀 Running Examples Summary

```bash
# Activate environment
myenv\Scripts\activate

# Run each example
python test0.py                    # Basic addition
python test1_commented_v1.py      # LLM Q&A
python test2.py                   # Blog generation
python test3.py                   # Parallel analysis
python test4_commented_v1.py      # Conditional routing
python test5.py                   # Human-in-the-loop

# Setup and run database examples
python seed_sqlite.py             # Setup SQLite
python seed_mongo.py              # Setup MongoDB
python multisource_langgraph.py   # Run multi-DB workflow

# View database contents
python read_sql.py                # View SQLite
python read_mongo.py              # View MongoDB
```

---

## 📖 Additional Resources

- **Detailed Documentation**: See `info.txt` for comprehensive information
- **Workflow Diagrams**: Check `workflow_diagrams/` folder for visual representations
- **Test Questions**: See `questions.json` for example queries
- **Reference Document**: `Canteen_Information.pdf`

---

## 🎯 Learning Outcomes

After completing this workshop, you'll be able to:

✅ Create LangGraph workflows from scratch
✅ Integrate LLMs into graph-based applications
✅ Design sequential and parallel workflows
✅ Implement conditional routing and branching
✅ Build human-in-the-loop interactive systems
✅ Integrate multiple databases with LLM-driven logic
✅ Handle state management effectively
✅ Optimize workflow performance
✅ Debug and troubleshoot graph workflows
✅ Apply patterns to real-world problems

---

## 📝 Project Details

- **Framework**: LangGraph
- **LLM Provider**: Azure OpenAI (GPT-4.1-mini)
- **Databases**: MongoDB, SQLite
- **Language**: Python 3.8+
- **Virtual Environment**: myenv/
- **Documentation**: Comprehensive with examples

---

## 🤝 Contributing

This is an educational workshop project. Suggestions for improvements:
- Add more example use cases
- Create additional exercises
- Expand database integration examples
- Add performance benchmarks

---

## 📄 License

This workshop project is provided for educational purposes.

---

## 🙋 Support

For issues or questions:
1. Check `info.txt` for detailed documentation
2. Review example files with comments
3. Check `Troubleshooting` section above
4. Examine workflow diagrams in `workflow_diagrams/`

---

**Happy Learning! 🚀**

*Last Updated: 2024*
*Version: 1.0*
