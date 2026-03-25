const leadService = require("../services/leadService");

exports.getLeads = async (req, res) => {
  try {
    const leads = await leadService.getAllLeads();
    res.json(leads);
  } catch (err) {
    res.status(500).json({ error: "Failed to fetch leads" });
  }
};

exports.updateStage = async (req, res) => {
  try {
    const { stage } = req.body;
    const updated = await leadService.updateLeadStage(
      req.params.id,
      stage
    );
    res.json(updated);
  } catch (err) {
    res.status(500).json({ error: "Failed to update stage" });
  }
};

exports.deleteLead = async (req, res) => {
  try {
    await leadService.deleteLead(req.params.id);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: "Failed to delete lead" });
  }
};