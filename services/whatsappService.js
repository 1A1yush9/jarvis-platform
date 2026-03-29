const axios = require("axios");

const sendWhatsApp = async (to, message) => {
  try {
    await axios.post(
      `https://api.twilio.com/2010-04-01/Accounts/${process.env.TWILIO_ACCOUNT_SID}/Messages.json`,
      new URLSearchParams({
        From: process.env.TWILIO_WHATSAPP_NUMBER,
        To: to,
        Body: message
      }),
      {
        auth: {
          username: process.env.TWILIO_ACCOUNT_SID,
          password: process.env.TWILIO_AUTH_TOKEN
        }
      }
    );
  } catch (err) {
    console.error("WhatsApp Error:", err.message);
  }
};

module.exports = sendWhatsApp;