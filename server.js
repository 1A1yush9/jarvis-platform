require("dotenv").config();

const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");
const fs = require("fs");

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// ================================
// 📁 SAFE FILE DATABASE (NO CRASH)
// ================================
const LEADS_FILE = "./leads.json";

if (!fs.existsSync(LEADS_FILE)) {
  fs.writeFileSync(LEADS_FILE, JSON.stringify([]));
}

function saveLead(data) {
  const leads = JSON.parse(fs.readFileSync(LEADS_FILE));
  leads.push(data);
  fs.writeFileSync(LEADS_FILE, JSON.stringify(leads, null, 2));
}

// ================================
// 🤖 GPT RESPONSE FUNCTION
// ================================
async function getAIResponse(userMessage) {
  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4o-mini",
        messages: [
          {
            role: "system",
            content:
              "You are a smart business assistant for a digital marketing agency. Convert users into leads. Be friendly, persuasive, and helpful.",
          },
          {
            role: "user",
            content: userMessage,
          },
        ],
      },
      {
        headers: {
          Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
        },
      }
    );

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error("GPT Error:", error.response?.data || error.message);
    return "Thanks for your message! Our team will contact you shortly.";
  }
}

// ================================
// 📩 TWILIO WHATSAPP WEBHOOK
// ================================
app.post("/webhook", async (req, res) => {
  const incomingMsg = req.body.Body;
  const userNumber = req.body.From;

  console.log("📩 Message:", incomingMsg);

  // 💾 SAVE LEAD
  saveLead({
    phone: userNumber,
    message: incomingMsg,
    timestamp: new Date(),
  });

  // 🤖 AI REPLY
  const aiReply = await getAIResponse(incomingMsg);

  // 📤 SEND RESPONSE (Twilio format)
  const twiml = `
    <Response>
      <Message>${aiReply}</Message>
    </Response>
  `;

  res.set("Content-Type", "text/xml");
  res.send(twiml);
});

// ================================
// 📊 LEADS API (FOR DASHBOARD)
// ================================
app.get("/leads", (req, res) => {
  const leads = JSON.parse(fs.readFileSync(LEADS_FILE));
  res.json(leads);
});

// ================================
app.listen(process.env.PORT, () => {
  console.log(`🚀 Server running on port ${process.env.PORT}`);
});