# Kala 🎭 — Performance • Knowledge • Revival

## 🌟 Why I Built This
Growing up around Indian classical art forms, I saw a huge challenge:  
- Performances often vanish after the stage lights go off.  
- Information about traditional arts is scattered in books (many not digitized, often complex language).  
- Dying and endangered art forms lack digital presence and revival efforts.  

*Kala* is my flagship project — a cultural platform that preserves, explains, and revives art forms.  
It solves a *real-world problem*: making performances, knowledge, and endangered arts accessible in one place, using modern web tech and AI.  

This project is also designed to *showcase my technical expertise* as a *full-stack developer and business analyst* who doesn’t just code, but builds solutions aligned with business impact.  

---

## 🧩 The Three Pillars of Kala
1. *Performance* — Watch curated videos of classical and folk performances, linked with metadata (artist, art form, year, rights, etc).  
2. *Ask Kala (AI-powered Information)* — Ask questions like “What is Bharatanatyam?” and get concise, easy-to-understand answers.  
   - Powered by NLP retrieval over an internal corpus of curated documents.  
3. *Revival* — Discover endangered or rare art forms with context, stories, and reference material.  

---

## ⚙ Tech Stack

*Frontend:*  
- React + Vite  
- Tailwind CSS (custom earthy brown & green theme, Georgia font, grid + card layouts)  
- Axios (API integration)  
- Netlify for hosting  

*Backend:*  
- Python (FastAPI for REST APIs)  
- SQLAlchemy + SQLite (for structured storage of performances & revival forms)  
- Pandas (for CSV ingestion/processing)  
- Scikit-learn (vectorization for document retrieval)  
- Render for hosting backend services  

*Other Tools:*  
- GitHub (version control & CI/CD)  
- Prompt engineering for improving AI retrieval and synthesis  
- Deployment with environment configs (VITE_API_URL)  

---

## 🚀 Process Followed
1. *Phase 0 – Setup*: Repo structure, database schema, seed data.  
2. *Phase 1 – Backend APIs*: Built Performances and Revival endpoints.  
3. *Phase 2 – AI Retriever*: Document ingestion, vectorization, cosine similarity search.  
4. *Phase 3 – Frontend Integration*: React pages (Home, Performances, Ask Kala, Revival).  
5. *Phase 4 – UI/UX Polish*: Earthy color scheme, centered grids, Georgia font, logo, improved aesthetics.  
6. *Phase 5 – QA & Fixes*: Fixed video links, improved search (fuzzy matching, synonyms).  
7. *Phase 6 – Deployment*:  
   - Backend → Render (https://kala-mvp.onrender.com/docs)  
   - Frontend → Netlify (https://kala.netlify.app)  
   - Connected via environment variables.  

---

## 🧗 Difficulties Faced & How I Solved Them
- *Problem:* 0 results for certain queries.  
  - *Solution:* Added interpolation, fuzzy search, and fallback strategies in retrieval.  
- *Problem:* Wrong video links in performances.  
  - *Solution:* Normalized YouTube embed links and updated seed data.  
- *Problem:* Deployment errors (requirements.txt missing, 404 root path).  
  - *Solution:* Added backend requirements.txt, pointed API routes correctly, configured Netlify publish directory.  
- *Problem:* AI answers sometimes mismatched (e.g., Odissi for Bharatanatyam).  
  - *Solution:* Improved preprocessing, retraining on larger corpus, prompt engineering for synthesis.  

Through this I demonstrated not just coding but *debugging, optimization, and applied AI problem-solving.*

---

## 🤖 AI & Prompt Engineering
This project also gave me hands-on experience in:  
- Crafting *retriever + generator pipelines* (vectorization + synthesis).  
- Writing prompts for *concise answers* (not dumping full paragraphs).  
- Balancing *data-driven search* with *AI interpretability*.  

This strengthens my ability to apply AI in *business analyst roles*, bridging technical implementation and product goals.  

---

## 🔮 Future Prospects
- Expand *knowledge base* with digitized books and Wikipedia API integration.  
- Support *multilingual answers* with translations.  
- Add *authentication & role-based uploads* (artists uploading performances).  
- Integrate *analytics dashboard* (which art forms are trending, which regions show revival interest).  
- Tours and offline events integration for revival campaigns.  

---


👉 In short: I don’t just build apps — I build *scalable, purposeful, and impactful solutions.*  

---

## 🌐 Live Demo
- *Frontend:* [Kala on Netlify](https://kala.netlify.app)  
- *Backend Docs:* [Kala API on Render](https://kala-mvp.onrender.com/docs)  

---
