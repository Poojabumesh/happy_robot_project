# 📞 Automated Load Matching Voice Agent  
**Client:** Acme Logistics  
**Engineer:** *Pooja Baralu Umesh*  

> An AI-powered voice agent that automates carrier load-matching, negotiates rates, and routes outcomes—reducing dispatcher workload while improving response accuracy and speed.

---

## 🚀 Overview
This project automates the **inbound load-matching workflow** for freight carriers using voice interaction on the HappyRobot platform. Instead of requiring human dispatchers to manually verify carriers, collect shipment details, search for loads, and negotiate pricing, this agent performs all steps autonomously and escalates only when necessary.

---

## ✅ Key Capabilities

### 🔐 MC Verification (FMCSA)
- Validates carrier identity using the **FMCSA DOT API**
- If inactive/rejected:
  - Requests an alternate MC number  
  - Dynamically re-queries FMCSA
- Maintains seamless conversational flow

### 🎙️ Voice-Driven Intake
Captures:
- Pickup location  
- Delivery location  
- Equipment type  
- Load weight  

### 🔎 Automated Load Matching
- Structured voice inputs sent to a **FastAPI** load-matching service (Render-hosted)
- Matches loads against a structured dataset

### 🤝 Rate Negotiation
- Negotiates pricing **up to 3 times**
- Routes based on:
  - Accepted
  - Countered
  - Rejected

### 👤 Fallback Scenarios
- Escalates unresolved calls to a live dispatcher
- Logs unsuccessful match attempts

### 📊 Analytics & Logging
- Logs MC status, sentiment, negotiation outcomes, duration, and call metadata to **Google Sheets**
- Visual dashboards built on **Retool** (auto-refresh)

---

## 🧠 Tech Stack

| Component | Technology |
|----------|-------------|
| Reasoning + Voice Agents | HappyRobot |
| Backend Service | FastAPI (Render) |
| External API | FMCSA DOT Verification |
| Data Source | CSV Load Dataset |
| Containerization | Docker |
| Logging | Google Sheets Webhook |
| Dashboard | Retool |

---

## 🔁 End-to-End Flow
1. Inbound call triggers the voice agent  
2. Agent performs **FMCSA MC** verification  
3. If verified, agent gathers shipment constraints  
4. Backend API returns matching loads  
5. Agent negotiates rate automatically  
6. Outcome routed to dispatcher or logged as no-match  
7. Google Sheet updates asynchronously  
8. Retool dashboard reflects metrics in near-real-time  

---

## 🖥️ Architecture Diagram (Conceptual)
Carrier Call → Voice Agent → FMCSA API → Intake
↓            ↓
FastAPI Load Matcher ← CSV Dataset
↓
Rate Negotiation Logic → Dispatcher / No-Match
↓
Google Sheets Logging → Retool Dashboard

---

## 🔗 Demo & Links

- **GitHub Repo:**  
  https://github.com/Poojabumesh/happy_robot_project

- **FastAPI Load Matcher (Render):**  
  https://happy-robot-project.onrender.com/docs

- **HappyRobot Voice Agent Workflow:**  
  https://v2.platform.happyrobot.ai/dfe-pooja/workflow/z2675golyx9x/editor/x9q35ull7730

- **Analytics Dashboard (Retool):**  
  https://poojabumesh.retool.com/apps/b47893e8-843a-11f0-a538-131b401e2563/Inbound%20Career%20Sales%20(Moved%20at%202025-08-28%2020%3A04%3A58.866)/page1

---

## 🔍 Future Enhancements
- Dynamic lane pricing models  
- Carrier relationship scoring  
- Automated email booking confirmations  
- Multi-language support  

---

## 🤝 Contributions
Feel free to open issues or suggestions via GitHub. PRs are welcome!

---

## 📧 Contact
**Pooja Baralu Umesh**  
ML/AI Engineer | Voice & Agentic Workflows  
San Francisco Bay Area, CA  
