# AI Mastery Hub: 从零到一的 AI 全栈开发之路

这是一个系统化记录 AI 学习历程、代码实践及工具探索的仓库。通过工程化的方式组织知识，实现从 Python 基础到复杂 AI Agent 应用的跨越。

---

## 🎯 核心目标

1. **构建工程化思维**：不只是写简单的脚本，而是以全栈开发的规范组织 AI 项目（Monorepo 逻辑）。
2. **沉淀工具资产**：将分散的 CLI 命令、AI 产品探索心得及工具配置转化为可复用的文档。
3. **实战驱动学习**：通过 Vue 3 + NestJS 的全栈集成，探索 AI 在业务场景（如 PDF 处理、自动化流）中的落地。

---

## 🗺️ 学习路线图 (Roadmap)

- [ ] **Phase 01: Python 基础与数据处理**
  - [ ] Python 核心语法与环境管理 (Venv/Conda)
  - [ ] Numpy/Pandas 数据清洗与分析实战
  - [ ] 爬虫基础与数据预处理
- [ ] **Phase 02: AI 工具链与提示工程 (CLI & MD)**
  - [ ] Claude Code, LangChain CLI 等工具配置手册
  - [ ] 结构化 Prompt (提示词) 框架与模板沉淀
  - [ ] AI 辅助编程工作流优化
- [ ] **Phase 03: 大模型开发进阶 (LLM Core)**
  - [ ] OpenAI / DeepSeek / Claude API 调用集成
  - [ ] LangChain & LangGraph 核心逻辑实现
  - [ ] 向量数据库 (Chroma/Pinecone) 与 RAG 架构实现
- [ ] **Phase 04: AI 全栈项目实战**
  - [ ] **PDF 智能查询系统**: 基于 NestJS 后端与 Vue 3 前端的二进制流处理与 AI 问答。
  - [ ] **自动化 Agent**: 利用 n8n 结合 AI 实现复杂的业务自动化闭环。

---

## 🛠️ 技术栈

- **编程语言**: Python 3.10+, TypeScript
- **AI 框架**: LangChain, LangGraph, OpenAI SDK
- **Web 架构**: Vue 3 (Frontend), NestJS (Backend), Vite
- **基础设施**: n8n (Automation), Vector DB, pnpm (Monorepo)
- **工程化工具**: ESLint, Prettier, Git Hooks

---

## 🚀 快速开始

### 1. 环境初始化

```bash
# 克隆仓库
git clone <your-repo-url>

# 配置 Python 虚拟环境
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# 安装前端/后端依赖
pnpm install
```
