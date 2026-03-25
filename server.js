require("dotenv").config();

const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");

const app = express();

// ✅ REQUIRED FOR TWILIO
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// ✅ ROUTE
app.post("/webhook", async (req, res) => {
  try {
    console.log("INCOMING:", req.body);

    const from = req.body.From;   // whatsapp:+91xxxx
    const body = req.body.Body;   // message text

    const twilio = require("twilio");
    const client = twilio(
      process.env.TWILIO_ACCOUNT_SID,
      process.env.TWILIO_AUTH_TOKEN
    );

    // ✅ SIMPLE TEST REPLY
    await client.messages.create({
      from: process.env.TWILIO_WHATSAPP_NUMBER,
      to: from,
      body: "✅ Jarvis Reply: Message received -> " + body
    });

    res.sendStatus(200);

  } catch (err) {
    console.log("ERROR:", err.message);
    res.sendStatus(500);
  }
});

// TEST ROUTE
app.get("/", (req, res) => {
  res.send("Server Working ✅");
});

// DB (optional but keep)
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log("Server running on " + PORT));