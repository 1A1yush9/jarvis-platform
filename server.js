const express = require("express");
const bodyParser = require("body-parser");
const twilio = require("twilio");
require("dotenv").config();

const app = express();

// ✅ CHECK ENV
if (!process.env.TWILIO_ACCOUNT_SID || !process.env.TWILIO_AUTH_TOKEN) {
  console.error("❌ Twilio ENV missing");
  process.exit(1);
}

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ✅ ROOT ROUTE (fix Not Found)
app.get("/", (req, res) => {
  res.send("🚀 Jarvis LIVE");
});

// ✅ TWILIO
const client = twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// ✅ WEBHOOK
app.post("/webhook", async (req, res) => {
  try {
    const msg = req.body.Body || "";
    const from = req.body.From;

    console.log("Incoming:", msg);

    let reply = "🤖 Jarvis ready!";

    if (msg.toLowerCase().includes("hello")) {
      reply = "👋 Hello from Jarvis!";
    }

    await client.messages.create({
      body: reply,
      from: "whatsapp:+14155238886",
      to: from,
    });

    res.send("OK");
  } catch (e) {
    console.error(e.message);
    res.status(500).send("Error");
  }
});

// ✅ PORT FIX
const PORT = process.env.PORT || 10000;

app.listen(PORT, () => {
  console.log("🚀 Running on port " + PORT);
});