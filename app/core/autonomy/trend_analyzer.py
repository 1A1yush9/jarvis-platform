class TrendAnalyzer:
    """
    Detects directional change from observer history.
    Minimal safe version (no ML yet).
    """

    def detect_trend(self, metric_history):

        if len(metric_history) < 3:
            return None

        # simple downward trend detection
        if metric_history[-1] < metric_history[-2] < metric_history[-3]:
            return "declining"

        if metric_history[-1] > metric_history[-2] > metric_history[-3]:
            return "improving"

        return None


trend_analyzer = TrendAnalyzer()
