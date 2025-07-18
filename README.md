# Groq + E2B Code Interpreter

[E2B](https://e2b.dev) Code Interpreter is an open-source SDK that provides secure, sandboxed environments for executing code generated by LLMs via Groq API. Built specifically for AI data analysts, coding applications, and reasoning-heavy agents, E2B enables you to both generate and execute code in a secure sandbox environment in real-time.

This template combines Groq's fast inference with E2B's secure code sandboxing for safe, real-time code interpretation.

## Overview

This application demonstrates how to use Groq API for AI-powered code generation combined with E2B's secure code execution environment. Built as a complete, end-to-end template that you can fork, customize, and deploy for your own AI code interpreter applications.

E2B (Execute to Build) provides secure, isolated sandbox environments for running AI-generated code, while Groq delivers sub-second response times for code generation tasks.

**Key Features:**
- **AI Code Generation:** Leverage Groq's fast inference for generating Python code from natural language prompts
- **Secure Code Execution:** Run generated code safely in E2B's isolated sandbox environments  
- **Real-time Results:** Get code output and execution logs instantly
- **Customizable Prompts:** Easy-to-modify system and user prompts for different coding tasks
- **Production Ready:** Built with proper error handling and environment configuration
- **Multi-Language Support:** Run both Python and JavaScript/TypeScript code in secure sandboxes
- Sub-second response times, efficient concurrent request handling, and production-grade performance powered by Groq

## Architecture

**Tech Stack:**
- **Backend:** Python with asyncio support OR Node.js
- **AI Code Generation:** Groq API (Llama 3.3 70B Versatile)
- **Code Execution:** E2B Code Interpreter sandboxes
- **Package Management:** UV (ultra-fast Python package installer) OR npm/yarn
- **Environment Management:** python-dotenv OR dotenv

## Quick Start

### Prerequisites
- Python 3.12+ OR Node.js 18+
- UV package manager ([Install UV](https://docs.astral.sh/uv/getting-started/installation/)) OR npm/yarn
- Groq API key ([Create a free GroqCloud account](https://console.groq.com))
- E2B API key ([Get one for free here](https://e2b.dev/docs))

### Setup

#### Python Setup
1. **Clone the repository**
   ```bash
   gh repo clone janzheng/groq-e2b-template
   cd groq-e2b-template/py-examples
   ```

2. **Install uv package manager**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies**
   ```bash
   uv sync  # Creates .venv and installs dependencies
   ```

4. **Create a `.env` file** and add your API keys:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   E2B_API_KEY=your-e2b-api-key-here
   ```

5. **Run the Python example**
   ```bash
   uv run main.py
   ```

#### JavaScript/Node.js Setup
1. **Clone the repository** (if not already done)
   ```bash
   gh repo clone janzheng/groq-e2b-template
   cd groq-e2b
   ```

2. **Navigate to the JavaScript examples folder**
   ```bash
   cd js-examples
   ```

3. **Install dependencies**
   ```bash
   npm install
   ```

4. **Create a `.env` file** and add your API keys:
   ```env
   GROQ_API_KEY=your-groq-api-key-here
   E2B_API_KEY=your-e2b-api-key-here
   ```

5. **Run the JavaScript examples**
   ```bash
   # Run the main Groq + E2B example (generates Python code with Groq, executes in E2B)
   npm start
   
   # Run the JavaScript code execution example (executes JavaScript/TypeScript in E2B)
   npm run js-example
   ```

## Usage Examples

### Python Code Generation and Execution
The main Python example generates Python code for statistical analysis:

```python
from dotenv import load_dotenv
from e2b_code_interpreter import Sandbox
from groq import Groq
import os

# Initialize clients
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
sbx = Sandbox()

# Generate code with Groq
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are a Python data scientist..."},
        {"role": "user", "content": "Generate random numbers and calculate statistics"},
    ],
)

# Execute in E2B sandbox
code = extract_code(response.choices[0].message.content)
execution = sbx.run_code(code)
print(execution.logs.stdout[0])
```

### JavaScript Examples

#### 1. AI-Generated Code Execution (`main.js`)
This example uses Groq to generate Python code and executes it in an E2B sandbox:

```javascript
import { Sandbox } from '@e2b/code-interpreter'
import { Groq } from 'groq-sdk'
import 'dotenv/config'

// Initialize clients
const client = new Groq({ apiKey: process.env.GROQ_API_KEY })
const sandbox = await Sandbox.create({ apiKey: process.env.E2B_API_KEY })

// Generate Python code with Groq
const response = await client.chat.completions.create({
    model: "llama-3.3-70b-versatile",
    messages: [
        { role: "system", content: "You are a Python data scientist..." },
        { role: "user", content: "Generate random numbers and show statistics" },
    ],
})

// Execute the generated Python code in E2B sandbox
const code = extractPythonCode(response.choices[0].message.content)
const execution = await sandbox.runCode(code)
console.log(execution.logs.stdout[0])
```

#### 2. Direct JavaScript/TypeScript Execution (`js-example.js`)
This example shows how to execute JavaScript/TypeScript code directly in E2B:

```javascript
import { Sandbox } from "@e2b/code-interpreter";
import "dotenv/config";

// Create sandbox
const sbx = await Sandbox.create({ apiKey: process.env.E2B_API_KEY });

// Install npm packages in the sandbox
await sbx.commands.run("npm install axios");

// Execute TypeScript code with external dependencies
const execution = await sbx.runCode(`
  import axios from "axios";
  
  const url: string = "https://api.github.com/status";
  const response = await axios.get(url);
  response.data;
`, { language: "ts" });

console.log(execution.logs.stdout[0]);
```

### Multi-Language Code Execution Capabilities

The E2B Code Interpreter sandbox supports multiple programming languages:

- **Python**: Perfect for data science, machine learning, and general scripting
- **JavaScript/TypeScript**: Great for web APIs, data processing, and modern JavaScript features
- **Package Management**: Install packages on-the-fly (pip for Python, npm for JavaScript)
- **Cross-Language Workflows**: Generate code in one language (e.g., using Groq) and execute in another

**Key Benefits:**
1. **Language Flexibility**: Use the JavaScript SDK to execute both Python and JavaScript code
2. **Package Ecosystem Access**: Install and use packages from npm, PyPI, and other repositories
3. **Secure Execution**: All code runs in isolated sandboxes regardless of the language
4. **Real-time Results**: Get immediate feedback from code execution across languages

### Customizing for Your Use Case

**Modify the System Prompt** in `py-examples/main.py` or `js-examples/main.js`:
```python
SYSTEM_PROMPT = """You are a Python expert. Generate code that:
1. [Your specific requirements]
2. [Additional constraints]
3. [Output format specifications]"""
```

**Change the User Prompt** for different tasks:
```python
USER_PROMPT = "Your custom coding task description here"
```

**Switch Groq Models** by updating:
```python
LLM_MODEL = "llama-3.3-70b-versatile"  # or other available models
```

**Execute Different Languages** in E2B:
```javascript
// Python execution
await sandbox.runCode(pythonCode, { language: "python" })

// JavaScript execution  
await sandbox.runCode(jsCode, { language: "js" })

// TypeScript execution
await sandbox.runCode(tsCode, { language: "ts" })
```

## Sandbox Features

E2B sandboxes provide:
- **Isolated Execution:** Code runs in secure, isolated environments
- **Multiple Languages:** Support for Python, JavaScript, TypeScript, and more
- **Package Installation:** Install packages from npm, PyPI, and other repositories
- **File System Access:** Read/write files within the sandbox
- **Network Access:** Controlled internet connectivity
- **Automatic Cleanup:** Sandboxes auto-terminate after 5 minutes of inactivity

## Customization

This template is designed to be a foundation for building AI code interpreters. Key areas for customization:

- **Model Selection:** Update Groq model configuration in `py-examples/main.py` or `js-examples/main.js`
- **Prompt Engineering:** Customize system and user prompts for specific coding tasks
- **Code Parsing:** Modify code extraction logic for different output formats
- **Language Selection:** Choose between Python, JavaScript, TypeScript execution
- **Error Handling:** Add robust error handling for production use
- **Sandbox Configuration:** Customize E2B sandbox settings and timeouts

## Next Steps

### For Developers
- **Create your free GroqCloud account:** Access official API docs, the playground for experimentation, and more resources via [Groq Console](https://console.groq.com)
- **Get E2B API access:** Sign up at [E2B](https://e2b.dev) for secure code execution environments
- **Build and customize:** Fork this repo and start customizing to build your own AI code interpreter
- **Get support:** Connect with other developers building on Groq at [Groq Developer Forum](https://community.groq.com)

### For Founders and Business Leaders
- **See enterprise capabilities:** This template showcases production-ready AI that can handle real-time code generation and execution workloads safely
- **Discuss your needs:** [Contact Groq's team](https://groq.com/enterprise-access/) to explore how Groq can accelerate your AI initiatives

## Security Considerations

- E2B sandboxes provide isolated execution environments
- Generated code runs in containers separate from your main system
- API keys should be stored securely in environment variables
- Consider implementing additional input validation for production use

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

Created with Groq for AI code generation and E2B for secure code execution.
