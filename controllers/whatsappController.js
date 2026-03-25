const Lead = require("../models/Lead");
const { generateReply } = require("../services/aiService");
const { sendWhatsAppMessage } = require("../services/whatsappService");

const handleIncomingMessage = async (req, res) => {
  try {
    console.log("📩 Incoming Twilio Data:", req.body);

    const from = req.body.From.replace("whatsapp:", "");
    const text = req.body.Body;

    // Find or create lead
    let lead = await Lead.findOne({ phone: from });

    if (!lead) {
      lead = await Lead.create({
        phone: from,
        name: "WhatsApp User",
        messages: []
      });
    }

    // Save incoming message
    lead.messages.push({ text, incoming: true });
    await lead.save();

    // AI reply
    const reply = await generateReply(text);

    // Send reply
    await sendWhatsAppMessage(from, reply);

    // Save outgoing
    lead.messages.push({ text: reply, incoming: false });
    await lead.save();

    res.sendStatus(200);

  } catch (error) {
    console.error("Webhook Error:", error.message);
    res.sendStatus(500);
  }
};

module.exports = { handleIncomingMessage };