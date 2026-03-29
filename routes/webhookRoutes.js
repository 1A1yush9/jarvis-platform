const express = require("express");
const router = express.Router();

const generateReply = require("../services/gptService");
const sendWhatsApp = require("../services/whatsappService");

const Lead = require("../models/Lead");

// TWILIO WEBHOOK
router.post("/whatsapp", async (req, res) => {
  try {
    const incomingMsg = req.body.Body;
    const from = req.body.From;

    console.log("Incoming:", incomingMsg);

    // GPT Reply
    const reply = await generateReply(incomingMsg);

    // Save lead
    await Lead.create({
      phone: from,
      message: incomingMsg,
      response: reply
    });

    // Send reply
    await sendWhatsApp(from, reply);

    res.sendStatus(200);
  } catch (err) {
    console.error(err);
    res.sendStatus(500);
  }
});

module.exports = router;