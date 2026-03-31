import express from "express";
import bodyParser from "body-parser";
import dotenv from "dotenv";
import fetch from "node-fetch";

dotenv.config();

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const PORT = process.env.PORT || 10000;

// ROOT
app.get("/", (req, res) => {
  res.send("SERVER LIVE ✅");
});

// WEBHOOK
app.post("/webhook", async (req, res) => {
  try {
    console.log("Incoming:", req.body);

    const userMsg = req.body.Body;

    if (!userMsg) {
      return res.send("OK");
    }

    const aiRes = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "llama3-8b-8192",
        messages: [{ role: "user", content: userMsg }]
      })
    });

    const aiData = await aiRes.json();
    const reply = aiData?.choices?.[0]?.message?.content || "Error";

    console.log("Reply:", reply);

    res.set("Content-Type", "text/xml");
    res.send(`
      <Response>
        <Message>${reply}</Message>
      </Response>
    `);

  } catch (err) {
    console.error("ERROR:", err);
    res.send("Error");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on ${PORT}`);
});