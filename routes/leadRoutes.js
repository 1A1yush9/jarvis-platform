const express = require("express");
const router = express.Router();
const Lead = require("../models/Lead");
const auth = require("../middleware/auth");

// ✅ GET USER LEADS ONLY (MULTI-USER FIX)
router.get("/", auth, async (req, res) => {
  try {
    const leads = await Lead.find({ userId: req.user.id })
      .sort({ createdAt: -1 });

    res.json(leads);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// ✅ CREATE LEAD (IMPORTANT FOR SAAS)
router.post("/", auth, async (req, res) => {
  try {
    const newLead = new Lead({
      ...req.body,
      userId: req.user.id // 🔥 KEY LINE
    });

    await newLead.save();

    res.json(newLead);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// UPDATE lead
router.put("/:id", auth, async (req, res) => {
  try {
    const updated = await Lead.findOneAndUpdate(
      { _id: req.params.id, userId: req.user.id },
      req.body,
      { new: true }
    );

    res.json(updated);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;