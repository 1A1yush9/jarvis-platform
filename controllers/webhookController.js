const { generateReply, analyzeIntent } = require("../services/aiService");
const { sendMessage } = require("../services/whatsappService");
const { createOrUpdateLead, updateLeadData } = require("../services/leadService");
const { createPaymentLink } = require("../services/paymentService");
const Conversation = require("../models/Conversation");
const logger = require("../utils/logger");

const handleWebhook = async (req, res) => {
  try {
    const entry = req.body.entry?.[0];
    const changes = entry?.changes?.[0];
    const messageData = changes?.value?.messages?.[0];

    if (!messageData) return res.sendStatus(200);

    const userMessage = messageData?.text?.body;
    if (!userMessage) return res.sendStatus(200);

    const phone = messageData.from;

    logger.info("Incoming Message", userMessage);

    // 1. Save Lead
    const lead = await createOrUpdateLead(phone, userMessage);

    // 2. Intent
    const intentData = analyzeIntent(userMessage);

    // 3. AI Reply
    let aiReply = await generateReply(userMessage, intentData.intent);

    // 🔥 4. PAYMENT TRIGGER
    if (intentData.intent === "buying") {
      const payment = await createPaymentLink(phone);

      aiReply += `\n\n👉 Complete your payment here:\n${payment.paymentLink}`;
    }

    // 5. Send
    await sendMessage(phone, aiReply);

    // 6. Conversation
    let convo = await Conversation.findOne({ phone });
    if (!convo) convo = await Conversation.create({ phone, messages: [] });

    convo.messages.push(
      { text: userMessage, from: "user", time: new Date() },
      { text: aiReply, from: "bot", time: new Date() }
    );

    await convo.save();

    // 7. Update Lead
    await updateLeadData(lead, intentData);

    res.sendStatus(200);
  } catch (error) {
    logger.error("Webhook Error", error.message);
    res.sendStatus(500);
  }
};

module.exports = { handleWebhook };