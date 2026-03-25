const router = require("express").Router();
const bcrypt = require("bcryptjs");
const Client = require("../models/Client");
const adminAuth = require("../middleware/adminAuth");

/* GET ALL CLIENTS */
router.get("/", adminAuth, async (req, res) => {
  const clients = await Client.find().select("-password");
  res.json(clients);
});

/* ADD CLIENT */
router.post("/", adminAuth, async (req, res) => {
  const { name, email, password, company } = req.body;

  const hashed = await bcrypt.hash(password, 10);

  const client = new Client({ name, email, password: hashed, company });
  await client.save();

  res.json({ msg: "Client added" });
});

/* UPDATE CLIENT */
router.put("/:id", adminAuth, async (req, res) => {
  await Client.findByIdAndUpdate(req.params.id, req.body);
  res.json({ msg: "Client updated" });
});

/* DELETE CLIENT */
router.delete("/:id", adminAuth, async (req, res) => {
  await Client.findByIdAndDelete(req.params.id);
  res.json({ msg: "Client deleted" });
});

/* RESET PASSWORD */
router.put("/reset/:id", adminAuth, async (req, res) => {
  const hashed = await bcrypt.hash(req.body.password, 10);
  await Client.findByIdAndUpdate(req.params.id, { password: hashed });

  res.json({ msg: "Password reset successful" });
});

/* ASSIGN ANALYTICS */
router.put("/analytics/:id", adminAuth, async (req, res) => {
  await Client.findByIdAndUpdate(req.params.id, {
    analytics: req.body
  });

  res.json({ msg: "Analytics updated" });
});

module.exports = router;