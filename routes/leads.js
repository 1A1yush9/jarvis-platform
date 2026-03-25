const express = require("express");
const router = express.Router();
const mongoose = require("mongoose");

// ✅ SAFE MODEL IMPORT (avoids path + reload errors)
let Lead;

try {
  Lead = mongoose.model("Lead");
} catch (e) {
  const LeadSchema = new mongoose.Schema({
    name: { type: String, default: "" },
    business: { type: String, default: "" },
    city: { type: String, default: "" },
    niche: { type: String, default: "" },
    contact: { type: String, default: "" },

    status: {
      type: String,
      enum: ["new", "contacted", "closed"],
      default: "new",
    },

    createdAt: {
      type: Date,
      default: Date.now,
    },
  });

  Lead = mongoose.model("Lead", LeadSchema);
}

///////////////////////////////////////////////////////
// ✅ ADD LEAD
///////////////////////////////////////////////////////
router.post("/add", async (req, res) => {
  try {
    const { name, business, city, niche, contact } = req.body;

     if (!business) {
     req.body.business = "Unknown Business";
   }

    const lead = new Lead({
      name,
      business,
      city,
      niche,
      contact,
    });

    await lead.save();

    res.json({
      success: true,
      message: "Lead added successfully",
      data: lead,
    });
  } catch (err) {
    console.error("ADD LEAD ERROR:", err.message);
    res.status(500).json({ error: "Server error while adding lead" });
  }
});

///////////////////////////////////////////////////////
// ✅ GET ALL LEADS
///////////////////////////////////////////////////////
router.get("/", async (req, res) => {
  try {
    const leads = await Lead.find().sort({ createdAt: -1 });

    res.json({
      success: true,
      count: leads.length,
      data: leads,
    });
  } catch (err) {
    console.error("GET LEADS ERROR:", err.message);
    res.status(500).json({ error: "Server error while fetching leads" });
  }
});

///////////////////////////////////////////////////////
// ✅ UPDATE STATUS
///////////////////////////////////////////////////////
router.put("/:id", async (req, res) => {
  try {
    const { status } = req.body;

    if (!["new", "contacted", "closed"].includes(status)) {
      return res.status(400).json({ error: "Invalid status value" });
    }

    const lead = await Lead.findByIdAndUpdate(
      req.params.id,
      { status },
      { new: true }
    );

    if (!lead) {
      return res.status(404).json({ error: "Lead not found" });
    }

    res.json({
      success: true,
      message: "Status updated",
      data: lead,
    });
  } catch (err) {
    console.error("UPDATE ERROR:", err.message);
    res.status(500).json({ error: "Server error while updating lead" });
  }
});

///////////////////////////////////////////////////////
// ✅ DELETE LEAD (extra safe for CRM use)
///////////////////////////////////////////////////////
router.delete("/:id", async (req, res) => {
  try {
    const lead = await Lead.findByIdAndDelete(req.params.id);

    if (!lead) {
      return res.status(404).json({ error: "Lead not found" });
    }

    res.json({
      success: true,
      message: "Lead deleted",
    });
  } catch (err) {
    console.error("DELETE ERROR:", err.message);
    res.status(500).json({ error: "Server error while deleting lead" });
  }
});

module.exports = router;