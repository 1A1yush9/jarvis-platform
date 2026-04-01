import express from "express";
import dotenv from "dotenv";

dotenv.config();

const app = express();

// CRITICAL: Twilio sends urlencoded
app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const PORT = process.env.PORT || 3000;

// ✅ HEALTH CHECK
app.get("/", (req, res) => {
  res.send("Jarvis Backend LIVE ✅");
});

// ✅ WEBHOOK (FINAL WORKING)
app.post("/webhook/whatsapp", async (req, res) => {
  try {
    console.log("🔥 WEBHOOK HIT");
    console.log("BODY:", req.body);

    const incomingMsg = req.body.Body;
    const from = req.body.From;

    if (!incomingMsg) {
      console.log("❌ No message");
      return res.sendStatus(200);
    }

    console.log(`📩 ${from}: ${incomingMsg}`);

    // 🤖 GROQ AI CALL (DIRECT FETCH)
    const aiRes = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.GROQ_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "llama3-70b-8192",
        messages: [
          { role: "system", content: "You are Jarvis, a smart AI business assistant." },
          { role: "user", content: incomingMsg }
        ]
      })
    });

    const data = await aiRes.json();

    let reply = "⚠️ AI not responding";

    if (data?.choices?.[0]?.message?.content) {
      reply = data.choices[0].message.content;
    }

    console.log("🤖 Reply:", reply);

    // ✅ TWILIO XML RESPONSE (MANDATORY)
    const twiml = `
<Response>
<Message>${reply}</Message>
</Response>`;

    res.set("Content-Type", "text/xml");
    res.send(twiml);

  } catch (error) {
    console.error("❌ ERROR:", error);
    res.sendStatus(200);
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});