const twilio = require("twilio");

const client = twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

const sendWhatsAppMessage = async (to, message) => {
  try {
    await client.messages.create({
      from: process.env.TWILIO_WHATSAPP_NUMBER, // whatsapp:+14155238886
      to: `whatsapp:${to}`,
      body: message
    });

    console.log("✅ Message sent to:", to);

  } catch (error) {
    console.error("❌ Twilio Send Error:", error.message);
  }
};

module.exports = { sendWhatsAppMessage };