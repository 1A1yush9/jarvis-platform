const express = require("express");
const router = express.Router();
const Lead = require("../models/Lead");

// TEST
router.get("/test", (req, res) => {
  res.json({ message: "Public API working ✅" });
});

// SAVE LEAD (FIXED)
router.post("/lead", async (req, res) => {
  try {
    console.log("BODY:", req.body); // DEBUG

    const { phone, message } = req.body;

    if (!phone || !message) {
      return res.status(400).json({
        error: "Phone and message required"
      });
    }

    const newLead = await Lead.create({
      phone,
      message,
      response: "Test response"
    });

    res.json({
      success: true,
      data: newLead
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Save failed" });
  }
});

module.exports = router;