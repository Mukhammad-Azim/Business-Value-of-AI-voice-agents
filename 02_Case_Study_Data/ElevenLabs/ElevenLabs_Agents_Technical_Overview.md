# ElevenLabs Agents — Technical Documentation Summary
## Source: https://elevenlabs.io/docs/conversational-ai/overview (Accessed April 17, 2026)

---

## Overview

ElevenAgents (now branded "ElevenLabs Agents") is a platform for building, deploying, and monitoring conversational voice AI agents. Agents accomplish tasks through natural dialogue — from quick requests to complex, open-ended workflows.

## Core Architecture (4 Components)

1. **Fine-tuned Speech-to-Text (ASR)** — real-time speech recognition
2. **Language Model (LLM)** — customer's choice of language model, or custom LLM integration
3. **Low-latency Text-to-Speech (TTS)** — 5,000+ voices, 70+ languages
4. **Proprietary Turn-Taking Model** — handles conversation timing, interruption, natural pauses

## Platform Capabilities

### Design and Configure
- **Workflows** — graph-based visual conversation design editor
- **System Prompt** — configurable agent behavior
- **Models** — choice of LLM (including custom / LLM cascading)
- **Conversation Flow** — structured dialogue management
- **Voice & Language** — multilingual, voice cloning, custom voices
- **Knowledge Base** — RAG integration for enterprise knowledge
- **Tools** — function calling / API integration with external systems
- **Personalization** — per-user customization
- **Authentication** — secure identity verification

### Deploy
- **Web** — React SDK, Widget, UI components
- **Mobile** — Swift SDK, Kotlin SDK, React Native SDK
- **Telephony** — SIP Trunking, Twilio native integration, batch calls
- **WhatsApp** integration
- **WebSocket API** — direct low-level integration
- **Events** — real-time event streaming

### Monitor and Optimize
- **Users** — user tracking and management
- **Smart Search** — conversation search and retrieval
- **Experiments** — A/B testing of agent configurations
- **Testing** — automated agent evaluation
- **Conversation Analysis** — quality metrics, audit logs
- **Analytics Dashboard** — performance tracking
- **Real-time Monitoring** — live agent observation
- **Privacy** — Zero Retention Mode, configurable data handling
- **Cost Optimization** — LLM cost management tools
- **CLI** — command-line interface for operations

### Advanced Features
- **Custom Models** — bring your own LLM
- **LLM Cascading** — multi-model orchestration
- **Post-call Webhooks** — event-driven integrations
- **Events API** — fine-grained event handling

---

## Enterprise Features (from elevenlabs.io/enterprise)

- **Security**: SOC2 and GDPR compliant; optional Zero Retention Mode; end-to-end encryption; HIPAA-eligible with BAA
- **Data Residency**: US, EU, and India options
- **Scalability**: Enterprise-grade infrastructure tested across largest AI Audio deployments
- **SSO & RBAC**: Okta, Azure AD, Google Workspace integration; workspace role management
- **Custom SLAs**: Available for mission-critical workloads
- **Dedicated Engineering Support**: Forward-deployed engineering team
- **Integrations**: Zapier, Stripe, Cal.com, Twilio, Zendesk, HubSpot (out of box)
- **Trusted by 10,000+ businesses** (as of 2026)

### Enterprise Case Studies (Published 2026):
- Better.com — mortgage origination (February 2026)
- Cisco Webex — AI Agents voice
- Razorpay — outbound merchant engagement
- Deutsche Telekom — network-integrated AI call assistant
- eDreams ODIGEO — conversational travel
- 3Shape — global dental support

---

## Key Pricing Architecture (from documentation)
- Per-usage model (API calls / minutes / characters)
- Burst pricing for sudden traffic spikes
- Enterprise custom pricing available

---

## Relevance to Thesis
This documentation confirms: (1) the 4-component pipeline architecture claimed in Chapter 4 is accurate; (2) ElevenLabs provides the enterprise security infrastructure (SOC2, GDPR, Zero Retention) required for financial services deployment; (3) the "Agent Workflows" feature supports the graph-based conversation design described for Betsy; (4) tool-calling capability enables the Tinman API integration pattern described in the case study.
