const Payment = require("../models/Payment");

exports.getStats = async (req, res) => {
  try {
    const userId = req.user.id;

    // TOTAL
    const total = await Payment.aggregate([
      { $match: { userId, status: "paid" } },
      { $group: { _id: null, total: { $sum: "$amount" } } }
    ]);

    // TODAY
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const todayData = await Payment.aggregate([
      {
        $match: {
          userId,
          status: "paid",
          paidAt: { $gte: today }
        }
      },
      { $group: { _id: null, total: { $sum: "$amount" } } }
    ]);

    // MONTH
    const startMonth = new Date(today.getFullYear(), today.getMonth(), 1);

    const monthData = await Payment.aggregate([
      {
        $match: {
          userId,
          status: "paid",
          paidAt: { $gte: startMonth }
        }
      },
      { $group: { _id: null, total: { $sum: "$amount" } } }
    ]);

    res.json({
      totalRevenue: total[0]?.total || 0,
      todayRevenue: todayData[0]?.total || 0,
      monthlyRevenue: monthData[0]?.total || 0
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Dashboard failed" });
  }
};