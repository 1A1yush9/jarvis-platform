// ===============================
// JARVIS FINAL SERVER (STABLE BUILD)
// ===============================

const express = require("express");
const dotenv = require("dotenv");
const fetch = require("node-fetch");
const bodyParser = require("body-parser");

dotenv.config();

const app = express();

// ===============================
// MIDDLEWARE (CRITICAL FOR TWILIO)
// ===============================
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ===============================
// ROOT ROUTE (HEALTH CHECK)
// ===============================
app.get("/", (req, res) => {
  res.send("🚀 Jarvis SaaS Backend LIVE");
});

// ===============================
// WEBHOOK ROUTE (WHATSAPP)
// ===============================
app.post("/webhook/whatsapp", async (req, res) => {
  console.log("🔥 WEBHOOK HIT");

  try {
    const incomingMsg = req.body.Body || "No message";
    const from = req.body.From || "Unknown";

    console.log("📩 Message:", incomingMsg);
    console.log("👤 From:", from);

    // ===============================
    // GROQ AI API
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
          { role: "system", content: "You are a smart WhatsApp assistant. Keep replies short and useful." },
          { role: "user", content: incomingMsg }
        ],
        temperature: 0.7
      })
    });

    const data = await aiResponse.json();

    let reply = "⚠️ AI not responding";

    if (data && data.choices && data.choices.length > 0) {
      reply = data.choices[0].message.content;
    }

    console.log("🤖 Reply:", reply);

    // ===============================
    // TWIML RESPONSE
    // ===============================
    res.set("Content-Type", "text/xml");
    res.send(`
      <Response>
        <Message>${escapeXml(reply)}</Message>
      </Response>
    `);

  } catch (error) {
    console.error("❌ ERROR:", error);

    res.set("Content-Type", "text/xml");
    res.send(`
      <Response>
        <Message>⚠️ Server error</Message>
      </Response>
    `);
  }
});

// ===============================
// XML SAFE FUNCTION
// ===============================
function escapeXml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

// ===============================
// START SERVER
// ===============================
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("🚀 Server running on port " + PORT);
});