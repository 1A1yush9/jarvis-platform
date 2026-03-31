// =======================
// JARVIS WHATSAPP AI SERVER (GROQ FREE VERSION)
// =======================

require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const axios = require("axios");
const bodyParser = require("body-parser");
const twilio = require("twilio");

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// =======================
// ENV VARIABLES
// =======================
const {
  MONGO_URI,
  GROQ_API_KEY,
  TWILIO_ACCOUNT_SID,
  TWILIO_AUTH_TOKEN,
  TWILIO_WHATSAPP_NUMBER
} = process.env;

// =======================
// TWILIO CLIENT
// =======================
const client = twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);

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
// GROQ AI FUNCTION (FREE)
// =======================
async function getAIReply(userMessage) {
  try {
    const response = await axios.post(
      "https://api.groq.com/openai/v1/chat/completions",
      {
        model: "llama3-8b-8192",
        messages: [
          {
            role: "system",
            content: "You are a smart business assistant. Reply short, clear, and helpful."
          },
          {
            role: "user",
            content: userMessage
          }
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
// WHATSAPP WEBHOOK
// =======================
app.post("/webhook/whatsapp", async (req, res) => {
  try {
    const incomingMsg = req.body.Body;
    const from = req.body.From;

    console.log("📩 Incoming:", incomingMsg);

    // AI reply
    const aiReply = await getAIReply(incomingMsg);

    // Save chat
    await Chat.create({
      user: from,
      message: incomingMsg,
      reply: aiReply
    });

    // Send reply
    await client.messages.create({
      body: aiReply,
      from: TWILIO_WHATSAPP_NUMBER,
      to: from
    });

    console.log("✅ Reply Sent:", aiReply);

    res.sendStatus(200);

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
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🔥 Server running on port ${PORT}`));