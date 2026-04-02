// ===============================
// ENTERPRISE SERVER (FINAL BUILD)
// WhatsApp + Twilio + Groq AI
// ===============================

import express from "express";
import dotenv from "dotenv";
import fetch from "node-fetch";
import bodyParser from "body-parser";

dotenv.config();

const app = express();

// ===============================
// IMPORTANT: Twilio requires URL-encoded parser
// ===============================
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ===============================
// HEALTH CHECK (Render uses this)
// ===============================
app.get("/", (req, res) => {
  res.send("🚀 Jarvis SaaS Backend LIVE");
});

// ===============================
// 🔥 MAIN WEBHOOK (CRITICAL)
// ===============================
app.post("/webhook/whatsapp", async (req, res) => {
  console.log("🔥 WEBHOOK HIT");

  try {
    const incomingMsg = req.body.Body || "";
    const from = req.body.From || "";

    console.log("📩 Message:", incomingMsg);
    console.log("👤 From:", from);

    // ===============================
    // GROQ AI CALL (OpenAI Compatible)
    // ===============================
    const aiResponse = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "llama3-70b-8192",
        messages: [
          {
            role: "system",
            content: "You are Jarvis, a smart business assistant for WhatsApp automation. Keep replies short, helpful, and professional."
          },
          {
            role: "user",
            content: incomingMsg
          }
        ],
        temperature: 0.7
      })
    });

    const data = await aiResponse.json();

    let replyText = "⚠️ AI error, try again.";

    if (data && data.choices && data.choices.length > 0) {
      replyText = data.choices[0].message.content;
    }

    console.log("🤖 AI Reply:", replyText);

    // ===============================
    // TWIML RESPONSE (MANDATORY)
    // ===============================
    const twimlResponse = `
      <Response>
        <Message>${escapeXml(replyText)}</Message>
      </Response>
    `;

    res.set("Content-Type", "text/xml");
    res.send(twimlResponse);

  } catch (error) {
    console.error("❌ ERROR:", error);

    const fallback = `
      <Response>
        <Message>⚠️ Server error. Please try again later.</Message>
      </Response>
    `;

    res.set("Content-Type", "text/xml");
    res.send(fallback);
  }
});

// ===============================
// XML ESCAPE (IMPORTANT)
// ===============================
function escapeXml(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

// ===============================
// SERVER START (Render PORT)
// ===============================
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});