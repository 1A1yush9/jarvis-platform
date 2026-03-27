// ===============================
// JARVIS FINAL BACKEND (CLEAN)
// ===============================

const express = require("express");
const bodyParser = require("body-parser");
const twilio = require("twilio");
require("dotenv").config();

const app = express();

// ===============================
// MIDDLEWARE
// ===============================
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ===============================
// ROOT CHECK (FOR RENDER TEST)
// ===============================
app.get("/", (req, res) => {
  res.send("🚀 Jarvis Backend Running Successfully");
});

// ===============================
// TWILIO CLIENT
// ===============================
const client = twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// ===============================
// WEBHOOK (WHATSAPP AUTO REPLY)
// ===============================
app.post("/webhook", async (req, res) => {
  try {
    const incomingMsg = req.body.Body || "";
    const from = req.body.From;

    console.log("📩 Incoming:", incomingMsg);

    let reply = "🤖 Jarvis: Welcome! How can I help you?";

    // ===============================
    // BASIC AI LOGIC (UPGRADE LATER)
    // ===============================
    if (incomingMsg.toLowerCase().includes("price")) {
      reply = "💰 Our pricing starts from $10/month.";
    } else if (incomingMsg.toLowerCase().includes("hello")) {
      reply = "👋 Hello! This is Jarvis AI assistant.";
    }

    // ===============================
    // SEND REPLY
    // ===============================
    await client.messages.create({
      body: reply,
      from: "whatsapp:+14155238886", // Twilio Sandbox
      to: from,
    });

    res.status(200).send("OK");
  } catch (error) {
    console.error("❌ Webhook Error:", error.message);
    res.status(500).send("Error");
  }
});

// ===============================
// SERVER START (IMPORTANT)
// ===============================
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});