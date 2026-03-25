const express = require("express");
const router = express.Router();

const Conversation = require("../models/Conversation");

// Get conversation by lead
router.get("/:leadId", async (req, res) => {
  try {
    const chats = await Conversation.find({ leadId: req.params.leadId });
    res.json(chats);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;