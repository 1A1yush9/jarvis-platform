const axios = require("axios");
const { OPENAI_API_KEY } = require("../config/env");
const logger = require("../utils/logger");

const analyzeIntent = (message) => {
  const msg = message.toLowerCase();

  if (msg.includes("price") || msg.includes("cost")) {
    return { intent: "pricing", score: 7 };
  }

  if (msg.includes("buy") || msg.includes("start")) {
    return { intent: "buying", score: 10 };
  }

  if (msg.includes("info") || msg.includes("details")) {
    return { intent: "information", score: 5 };
  }

  return { intent: "general", score: 3 };
};

const generateReply = async (message, intent) => {
  try {
    let systemPrompt = "";

    if (intent === "buying") {
      systemPrompt = `
You are a sales closer.

User is ready to buy.
Push for immediate payment.

Reply:
- Strong CTA
- Urgency
- Short message
`;
    } else {
      systemPrompt = `
You are a sales assistant.

Goal:
Move user toward buying.
Ask 1 question.
Keep it short.
`;
    }

    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      {
        model: "gpt-4o-mini",
        messages: [
          { role: "system", content: systemPrompt },
          { role: "user", content: message }
        ]
      },
      {
        headers: {
          Authorization: `Bearer ${OPENAI_API_KEY}`,
          "Content-Type": "application/json"
        }
      }
    );

    return response.data.choices[0].message.content;
  } catch (error) {
    logger.error("AI ERROR", error.message);
    return "Let me help you get started quickly!";
  }
};

module.exports = { generateReply, analyzeIntent };