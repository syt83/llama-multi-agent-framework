# llama-multi-agent-framework
로컬 LLM(Qwen + llama.cpp)을 기반으로  
Boss-Agent + Worker-Agent 구조를 구현한 멀티 에이전트 AI 시스템

## 🎯 Problem

기존 LLM API 방식은 다음과 같은 한계가 있음:

- 하나의 모델이 모든 작업을 처리 → 품질 한계
- 복잡한 작업 분해 불가능
- 병렬 처리 구조 부재
- 로컬 환경에서 확장성 부족

## 💡 Solution

이를 해결하기 위해 다음 구조를 설계:

- Boss Agent: 작업 분해 및 계획
- Worker Agents: 역할별 병렬 실행
- Synthesizer: 결과 통합

- ## 🏗 Architecture
```
User Request
   ↓
Boss Agent (Task Planning)
   ↓
Worker Pool (Parallel Execution)
   ├── Code Worker
   ├── Research Worker
   ├── Writer Worker
   ↓
Synthesizer (Final Answer)
   ↓
Response
```
## ⚙️ Features

- 🧠 Multi-Agent Architecture (Boss + Workers)
- ⚡ Parallel execution using asyncio
- 🧩 Dynamic task decomposition
- 🔄 Role-based task routing
- 💬 LLM-based reasoning (Qwen 2.5 via llama.cpp)
- 🖥 REST API via FastAPI

- ## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

Start llama.cpp server
cd E:\llama.cpp\build\bin\Release
E:\llama.cpp\build\bin\Release\llama-server.exe ^
-m E:\my_agent_system\models\qwen2.5-3b.gguf ^
--port 8080

Run FastAPI server
venv\Scripts\activate
uvicorn main:app --reload --port 8001

Test API
GET http://127.0.0.1:8001/agent-chat
```


---

# 🚀 6. 기술적 포인트 (이게 핵심 차별점)

```md id="g7m2qp"
## 🔬 Technical Highlights

### 1. Multi-Agent Orchestration
단일 LLM이 아니라 역할 기반 에이전트 구조 설계

### 2. Parallel Execution
asyncio.gather를 이용한 Worker 병렬 처리

### 3. Local LLM Integration
OpenAI 없이 llama.cpp 기반 로컬 추론 시스템

### 4. Task Decomposition
LLM이 스스로 작업을 분해하는 구조 (Boss Agent)
```
