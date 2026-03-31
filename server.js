// =======================
// JARVIS WHATSAPP AI SERVER (FINAL CLEAN VERSION)
// =======================

require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const axios = require("axios");
const bodyParser = require("body-parser");
const { twiml } = require("twilio");

const MessagingResponse = twiml.MessagingResponse;

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// =======================
// ENV VARIABLES
// =======================
const {
  MONGO_URI,
  GROQ_API_KEY
} = process.env;

// =======================
// DATABASE CONNECT
// =======================
mongoose.connect(MONGO_URI)
  .then(() => console.log("✅ MongoDB Connected"))
  .catch(err => console.error("❌ Mongo Error:", err));

// =======================
// SCHEMA
// =======================
const ChatSchema = new mongoose.Schema({
  user: String,
  message: String,
  reply: String,
  createdAt: { type: Date, default: Date.now }
});

const Chat = mongoose.model("Chat", ChatSchema);

// =======================
// GROQ AI FUNCTION
// =======================
async function getAIReply(userMessage) {
  try {
    const response = await axios.post(
      "https://api.groq.com/openai/v1/chat/completions",
      {
        model: "llama3-8b-8192",
        messages: [
          { role: "system", content: "Reply short, smart, business-focused." },
          { role: "user", content: userMessage }
        ],
        max_tokens: 150
      },
      {
        headers: {
          Authorization: `Bearer ${GROQ_API_KEY}`,
          "Content-Type": "application/json"
        }
      }
    );

    return response.data.choices[0].message.content;

  } catch (error) {
    console.error("❌ GROQ ERROR:", error.response?.data || error.message);
    return "⚠️ AI temporarily unavailable.";
  }
}

// =======================
// WHATSAPP WEBHOOK (FINAL)
// =======================
app.post("/webhook/whatsapp", async (req, res) => {
  try {
    const incomingMsg = req.body.Body;
    const from = req.body.From;

    console.log("📩 Incoming:", incomingMsg);

    const aiReply = await getAIReply(incomingMsg);

    await Chat.create({
      user: from,
      message: incomingMsg,
      reply: aiReply
    });

    const twimlResponse = new MessagingResponse();
    twimlResponse.message(aiReply);

    res.writeHead(200, { "Content-Type": "text/xml" });
    res.end(twimlResponse.toString());

  } catch (error) {
    console.error("❌ Webhook Error:", error);
    res.sendStatus(500);
  }
});

// =======================
// HEALTH CHECK
// =======================
app.get("/", (req, res) => {
  res.send("🚀 Jarvis AI (Groq Free) is LIVE");
});

// =======================
const PORT = process.env.PORT || 10000;
app.listen(PORT, () => console.log(`🔥 Server running on port ${PORT}`));