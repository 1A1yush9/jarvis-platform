const express = require("express");
const bodyParser = require("body-parser");

const app = express();

// REQUIRED for Twilio
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ROOT CHECK
app.get("/", (req, res) => {
  res.send("🚀 Jarvis SaaS Backend LIVE");
});

// 🔥 WEBHOOK (FINAL FIX)
app.post("/webhook/whatsapp", (req, res) => {
  console.log("🔥 WEBHOOK HIT");

  const msg = req.body.Body || "No message";

  console.log("Message:", msg);

  res.set("Content-Type", "text/xml");
  res.send(`
    <Response>
      <Message>Reply: ${msg}</Message>
    </Response>
  `);
});

// START SERVER
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("🚀 Server running on port " + PORT);
});