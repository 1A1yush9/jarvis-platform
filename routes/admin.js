const express = require("express");
const router = express.Router();
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/User");
const { verifyToken, verifyAdmin } = require("../middleware/auth");

/* ================= ADMIN LOGIN ================= */
router.post("/login", async (req, res) => {
  const { email, password } = req.body;

  const admin = await User.findOne({ email, role: "admin" });
  if (!admin) return res.status(404).json({ message: "Admin not found" });

  const valid = await bcrypt.compare(password, admin.password);
  if (!valid) return res.status(401).json({ message: "Wrong password" });

  const token = jwt.sign({ id: admin._id, role: admin.role }, "jarvis_secret");

  res.json({ token });
});

/* ================= GET ALL CLIENTS ================= */
router.get("/clients", verifyToken, verifyAdmin, async (req, res) => {
  const clients = await User.find({ role: "client" });
  res.json(clients);
});

/* ================= ADD CLIENT ================= */
router.post("/clients", verifyToken, verifyAdmin, async (req, res) => {
  const { name, email, password } = req.body;

  const hash = await bcrypt.hash(password, 10);

  const user = new User({
    name,
    email,
    password: hash,
    role: "client"
  });

  await user.save();
  res.json({ message: "Client added" });
});

/* ================= UPDATE CLIENT ================= */
router.put("/clients/:id", verifyToken, verifyAdmin, async (req, res) => {
  await User.findByIdAndUpdate(req.params.id, req.body);
  res.json({ message: "Updated" });
});

/* ================= DELETE CLIENT ================= */
router.delete("/clients/:id", verifyToken, verifyAdmin, async (req, res) => {
  await User.findByIdAndDelete(req.params.id);
  res.json({ message: "Deleted" });
});

/* ================= RESET PASSWORD ================= */
router.put("/reset/:id", verifyToken, verifyAdmin, async (req, res) => {
  const hash = await bcrypt.hash(req.body.password, 10);
  await User.findByIdAndUpdate(req.params.id, { password: hash });
  res.json({ message: "Password reset" });
});

/* ================= ASSIGN ANALYTICS ================= */
router.put("/analytics/:id", verifyToken, verifyAdmin, async (req, res) => {
  await User.findByIdAndUpdate(req.params.id, {
    analytics: req.body.analytics
  });
  res.json({ message: "Analytics assigned" });
});

module.exports = router;