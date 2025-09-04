// src/api.js
import axios from "axios";

// Reads your backend URL from .env (we set this already)
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export async function getPerformances(params = {}) {
  const res = await axios.get(`${API_URL}/api/performances`, { params });
  return res.data;
}

export async function getPerformance(id) {
  const res = await axios.get(`${API_URL}/api/performances/${id}`);
  return res.data;
}

export async function getRevival(params = {}) {
  const res = await axios.get(`${API_URL}/api/revival`, { params });
  return res.data;
}

export async function askKala(query) {
  const res = await axios.post(`${API_URL}/api/ask`, { query });
  return res.data;
}
