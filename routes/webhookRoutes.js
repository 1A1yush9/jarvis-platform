const express = require("express");
const router = express.Router();

const { handleIncomingMessage } = require("../controllers/whatsappController");

router.post("/webhook", handleIncomingMessage);

module.exports = router;