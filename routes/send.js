const express = require("express");
const router = express.Router();

// IMPORTANT: this handles /api/send/campaign
router.post("/campaign", (req, res) => {
  console.log("✅ Campaign API Hit");
  console.log("BODY:", req.body);

  res.json({
    success: true,
    message: "Campaign working",
    data: req.body
  });
});

module.exports = router;