const express = require("express");
const router = express.Router();
const OpenAI = require("openai");

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

router.post("/generate", async (req, res) => {
  try {
    const { business, city, niche } = req.body;

    const prompt = `
Write a short cold outreach message for a ${niche} business in ${city}.
Business name: ${business}.
Make it friendly and conversion-focused.
`;

    const response = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }],
    });

    res.json({
      message: response.choices[0].message.content,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;